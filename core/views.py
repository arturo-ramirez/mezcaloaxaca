from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def acercade(request):
    return render(request, 'core/acercade.html')


def proceso(request):
    return render(request, 'core/proceso.html')


def venta(request):
    return render(request, 'core/venta.html')
