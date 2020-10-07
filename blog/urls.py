from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('webhook/', views.webhook),
]