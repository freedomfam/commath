from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('32bit/', views.decto32fp),
    path('64bit/', views.decto64fp),
    path('AxBs/', views.AxBs),

    path('differentiation/', views.differentiation),
    path('integration/', views.integration),
    path('rootfinding/', views.rootfinding),
]
