from django.urls import path
from . import views

app_name = 'repair'
urlpatterns = [
    path('', views.index, name='index'),
    path('python/', views.pythonsoft, name='hardware'),
    path('django/', views.djangosoft, name='software'),
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('softdetail/<str:pk>/', views.softdetail, name='softdetail'),

    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfoliodetails/<str:pk>/', views.portfoliodetail, name='portfoliodetail'),
]
