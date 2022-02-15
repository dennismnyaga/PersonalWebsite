from multiprocessing import context
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'repair/index.html', context)

