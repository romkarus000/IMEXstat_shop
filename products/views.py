from django.views import generic
from .models import Research
from personal_cabinet.models import Client
from orders.models import Order
from .mixins import CategoryContextMixin
from django.urls import reverse
from .forms import ResearchBuyForm
from seo.mixins.views import ModelInstanceViewSeoMixin
from django.http import JsonResponse


def autocomplete(request):
    if request.is_ajax():
        queryset = Research.objects.filter(title__icontains=request.GET.get('search'))
        research_list = []
        for i in queryset:
            research_list.append(i.title)
        data = {
            'list': research_list
        }
        return JsonResponse(data)


class ResearchListView(generic.ListView, CategoryContextMixin):
    context_object_name = 'researchs'

    def get_queryset(self):
        if self.request.GET.get('research'):
            return Research.objects.filter(title__icontains=self.request.GET.get('research'))
        else:
            try:
                return Research.objects.filter(research_type=self.kwargs['type'])
            except KeyError:
                return Research.objects.all()


class ResearchCategoryListView(generic.ListView, CategoryContextMixin):
    context_object_name = 'researchs'

    def get_queryset(self):
        return Research.objects.filter(category__slug=self.kwargs['slug'])


class ResearchDetailView(ModelInstanceViewSeoMixin, generic.DetailView, CategoryContextMixin):
    model = Research


'''class ResearchFormBuyView(generic.FormView):
    form_class = ResearchBuyForm
    success_url = "/"

    def form_valid(self, form):
        client = Client.objects.get(user=self.request.user)
        Order.objects.create(client=client)
        order = Order.objects.latest()
        form.research = Research.objects.get(slug=self.kwargs['slug'])
        form.order = order
        form.save()

        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        if self.success_url:
            url = self.success_url % self.object.__dict__
'''


class ResearchBuyView(generic.edit.FormMixin, ModelInstanceViewSeoMixin, generic.DetailView, CategoryContextMixin):
    model = Research
    form_class = ResearchBuyForm
    template_name = 'products/research_buy.html'

    def get_success_url(self):
        return reverse('research:list')

    def get_context_data(self, *args, **kwargs):
        context = super(ResearchBuyView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        client = Client.objects.get(user=self.request.user)
        Order.objects.create(client=client)
        order = Order.objects.latest()
        order_cart = form.save(commit=False)
        order_cart.order = order
        order_cart.research = Research.objects.get(slug=self.kwargs['slug'])
        order_cart.save()
        return super().form_valid(form)


