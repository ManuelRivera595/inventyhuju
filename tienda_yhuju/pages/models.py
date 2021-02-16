from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="order", default=0)
    decimal = models.DecimalField(verbose_name="Kilogramo",max_digits=6, decimal_places=2)
    pcompra = models.DecimalField(verbose_name="Precio Compra",max_digits=6, decimal_places=2)
    pventa = models.DecimalField(verbose_name="Precio Venta",max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
