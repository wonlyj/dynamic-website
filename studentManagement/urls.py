from django.urls import path
from studentManagement import views
from django.urls import re_path as url
app_name = 'studentManager'
urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('regist/', views.regist, name='regist'),
    path('logout/', views.logout, name='logout'),
    path('add/', views.add, name='add'),
    path('select/', views.select, name='select'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('new_studentinformation/', views.new_studentinformation, name='new_studentinformation'),
]
