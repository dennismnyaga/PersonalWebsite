from django.shortcuts import render
from .models import *

def index(request):
    hard = Pythonister.objects.order_by('-date_added')
    soft = Djangonister.objects.order_by('-date_added')
    context = {'hard':hard, 'soft':soft}
    return render(request, 'repair/index.html', context)

def pythonsoft(request):
    hard = Pythonister.objects.order_by('-date_added')
    context = {'hard':hard}
    return render(request, 'repair/hardware.html', context)

def djangosoft(request):
    soft = Djangonister.objects.order_by('-date_added')
    context = {'soft':soft}
    return render(request, 'repair/django.html', context)


def detail(request, pk):
    hard = Pythonister.objects.get(id=pk)
    context = {'hard':hard}
    return  render(request, 'repair/detail.html', context)

def softdetail(request, pk):
    soft = Djangonister.objects.get(id=pk)
    context = {'soft':soft}
    return  render(request, 'repair/softdetail.html', context)


def portfolio(request):
    soft = Portfolio.objects.order_by('-date_added')
    context = {'soft':soft}
    return render(request, 'repair/portfolio.html', context)

def portfoliodetail(request, pk):
    soft = Portfolio.objects.get(id=pk)
    context = {'soft':soft}
    return  render(request, 'repair/portfoliodetail.html', context)