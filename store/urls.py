from django.urls import path

from bookstore.urls import urlpatterns
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),

]
