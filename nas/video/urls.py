from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug>/', views.detail),
    path('<slug>/<id>/', views.video),
]
