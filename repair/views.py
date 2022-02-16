from django.shortcuts import render
from .models import *

def index(request):
    hard = Hardware.objects.order_by('-date_added')
    soft = Software.objects.order_by('-date_added')
    context = {'hard':hard, 'soft':soft}
    return render(request, 'repair/index.html', context)

def hardware(request):
    hard = Hardware.objects.order_by('-date_added')
    context = {'hard':hard}
    return render(request, 'repair/hardware.html', context)

def software(request):
    soft = Software.objects.order_by('-date_added')
    context = {'soft':soft}
    return render(request, 'repair/software.html', context)


def detail(request, pk):
    hard = Hardware.objects.get(id=pk)
    soft = Software.objects.get(id=pk)
    context = {'hard':hard, 'soft':soft}
    return  render(request, 'repair/detail.html', context)