from django.urls import path
from app1 import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('get_massage',views.get_massage),
]
