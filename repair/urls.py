from django.urls import path
from . import views

app_name = 'repair'
urlpatterns = [
    path('', views.index, name='index'),
    path('hardware/', views.hardware, name='hardware'),
    path('software/', views.software, name='software'),
    path('detail/<str:pk>/', views.detail, name='detail'),
]
