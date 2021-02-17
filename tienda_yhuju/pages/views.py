from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils.html import strip_tags #excel
from openpyxl import Workbook  #excel
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

#Nuestra clase hereda de la vista genérica TemplateView
class ReporteExcel(TemplateView):
     
    #Usamos el método get para generar el archivo excel 
    def get(self, request, *args, **kwargs):
        #Obtenemos todas las pages de nuestra base de datos
        pages = Page.objects.all()
        #Creamos el libro de trabajo
        wb = Workbook()
        #Definimos como nuestra hoja de trabajo, la hoja activa, por defecto la primera del libro
        ws = wb.active
        #En la celda B1 ponemos el texto 'REPORTE DE PERSONAS'
        ws['B1'] = 'INVENTARIO'
        #Juntamos las celdas desde la B1 hasta la E1, formando una sola celda
        ws.merge_cells('B1:H1')
        #Creamos los encabezados desde la celda B3 hasta la E3
        ws['B3'] = 'ID'
        ws['C3'] = 'PRODUCTO'
        ws['D3'] = 'DETALLE'
        ws['E3'] = 'CANT|UND'
        ws['F3'] = 'CANT|KG'
        ws['G3'] = 'PRECIO COMPRA'
        ws['H3'] = 'PRECIO VENTA'       
        cont=5
        #Recorremos el conjunto de personas y vamos escribiendo cada uno de los datos en las celdas
        for page in pages:
            ws.cell(row=cont,column=2).value = page.id
            ws.cell(row=cont,column=3).value = page.title
            ws.cell(row=cont,column=4).value = strip_tags(page.content)
            ws.cell(row=cont,column=5).value = page.order
            ws.cell(row=cont,column=6).value = page.decimal
            ws.cell(row=cont,column=7).value = page.pcompra
            ws.cell(row=cont,column=8).value = page.pventa
            cont = cont + 1
        #Establecemos el nombre del archivo
        nombre_archivo ="ReporteExcel.xlsx"
        #Definimos que el tipo de respuesta a devolver es un archivo de microsoft excel
        response = HttpResponse(content_type="application/ms-excel") 
        contenido = "attachment; filename={0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        wb.save(response)
        return response

#fin formato Excel
