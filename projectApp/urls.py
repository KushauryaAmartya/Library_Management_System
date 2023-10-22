from django.contrib import admin
from django.urls import path,include

from projectApp import views

urlpatterns = [
   
    path("",views.home,name=''),
    path("home",views.home,name='home'),
    path("add",views.add,name='add'),
    path("display",views.display,name='display'),
    path('edit-book/<str:bookid>/', views.edit, name='edit_book'),
    path('delete-book/', views.delete, name='delete_book')
]