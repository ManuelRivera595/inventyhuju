from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm

#staff
class StaffRequiredMixin(object):
    """
    Usuario miembro del staff
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    

# Create your views here.
class PageListView(StaffRequiredMixin, ListView):
    model = Page

class PageDetailView(StaffRequiredMixin, DetailView):
    model = Page

class PageCreate(StaffRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

class PageUpdate(StaffRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

# buscador
class BuscarView(TemplateView):
    def post(self, request, *args, **kwargs):
        buscar=request.POST['buscalo']
        pages = Page.objects.filter(title__contains=buscar.upper())
        return render(request, 'pages/buscar.html',
                    {'pages':pages, 'page':True})