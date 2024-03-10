from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound, HttpResponse, Http404
# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def hi(request):
    return render(request, 'blog/hi.html')


def categ(request, catid):
    if request.GET:
        print('Имя:', request.GET['name'])
        print('Возраст:', request.GET['age'])
    # if request.GET:
    #     if request.GET['password'] == '12345':
    #         print('Доступ открыт')
    #     else:
    #         print('Иди нахуй сука')
    #     print(request.GET)
    # else:
    #     print('Нет данных')
    if int(catid) == 50:
        raise Http404 # ручная генерация ошибки
    if int(catid) == 1000:
        return redirect('home')  # перенаправление
    if int(catid) == 600:
        return redirect('hi', permanent=True)
    return HttpResponse(f"<h1>Page {catid}</h1>")


def pageNotFound(request, exception):
    print(exception, "***")
    return HttpResponseNotFound('<h1>Страница не найдена:(</h1>')
