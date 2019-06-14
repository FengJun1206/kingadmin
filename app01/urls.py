from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path('', views.index, name='index'),


    # path('login/', views.acc_login, name='login'),
    # path('logout/', views.acc_logout, name='logout'),
]