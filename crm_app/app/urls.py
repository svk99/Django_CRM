from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('home/',home),
    path('add/',add),
    path('delete/<int:id>',delete),
    path('update/<int:id>',update),
    path('do_update/<int:id>', do_update),
    path('delete_all/', delete_all, name='delete_all')
]