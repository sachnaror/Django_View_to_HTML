from django.urls import path

from .views import index, my_view

urlpatterns = [
    path('', index, name='index'),
    path('my_view/', my_view, name='my_view')
]
