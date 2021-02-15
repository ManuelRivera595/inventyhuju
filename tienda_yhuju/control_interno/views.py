from django.shortcuts import render, HttpResponse

def control_interno(request):
    return render(request, "core/index.html")

def proceso_interno(request):
    return render(request, "core/procesos.html")


