from django.urls import path
from .views import category_list, category_add

urlpatterns = [
    path('categories/', category_list),
    path('categories/add/', category_add)
]