from django import forms
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order', 'decimal', 'pcompra', 'pventa']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Producto'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cantidad-Unidad'}),
            'decimal': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cantidad-Kilos'}),
            'pcompra': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio Compra'}),
            'pventa': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio Venta'}),
        }
        labels = {
            'title':'', 'content':'', 'order':'', 'decimal':'', 'pcompra':'', 'pventa':''
        }