from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name = 'home'),
    path('hi/',views.hi,name = 'hi'),
    path("categ/<int:catid>/",views.categ,name ='categ')
]
