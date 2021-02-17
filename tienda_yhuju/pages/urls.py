from django.urls import path
from .views import PageListView, PageDetailView, PageCreate, PageUpdate, PageDelete
from .views import BuscarView, ReporteExcel

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PageDelete.as_view(), name='delete'),
    path('buscar/',BuscarView.as_view(), name="buscar"),
    path('reporte_excel/',ReporteExcel.as_view(), name="reporte_excel"),
], 'pages')