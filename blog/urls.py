from django.urls import path
from . import views

# Este padrão dirá ao Django que views.post_list é o lugar correto aonde ir se alguém entra em seu site pelo endereço
# 'http://127.0.0.1:8000 /'.

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
