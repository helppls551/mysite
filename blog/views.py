from django.shortcuts import render
from django.http import HttpResponseNotFound,HttpResponse
# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def hi(request):
    return render(request, 'blog/hi.html')

def categ(request,catid):
    return HttpResponse(f"<h1>Page {catid}</h1>")
def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')