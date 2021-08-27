from django.shortcuts import render
from django.http import HttpResponse
from .. import templates
def index(request):
    return render(request, 'base.html', None)
