from django.urls import reverse
from django.views.generic import TemplateView, RedirectView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Building


class HomeView(TemplateView):
    template_name = "buildings/index.html"


class SortDefaultView(RedirectView):
    # url = reverse('buildings:sort-by-name')

    def get_redirect_url(self, *args, **kwargs):
        return reverse('buildings:sort-by-name')


class SortPkView(ListView):
    template_name = 'buildings/sort-by-pk.html'

    def get_queryset(self):
        return Building.objects.order_by('-pk')


class SortNameView(ListView):
    template_name = 'buildings/sort-by-name.html'

    def get_queryset(self):
        return Building.objects.order_by('name')


class NewBuildingView(CreateView):
    template_name = 'buildings/create.html'
    model = Building
    fields = [
        'name',
        'country',
        'city',
        'street',
        'number',
        'floors',
        'color',
        'residential',
    ]

    def get_success_url(self):
        return reverse('buildings:sort-by-pk')


class DetailBuildingView(DetailView):
    template_name = 'buildings/read.html'
    model = Building


class ModifyBuildingView(UpdateView):
    template_name = 'buildings/update.html'
    model = Building
    fields = [
        'name',
        'country',
        'city',
        'street',
        'number',
        'floors',
        'color',
        'residential',
    ]


class DeleteBuildingView(DeleteView):
    template_name = 'buildings/delete.html'
    model = Building
    # success_url = reverse('buildings:create')

    def get_success_url(self):
        return reverse('buildings:sort-by-name')
