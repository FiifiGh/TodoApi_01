from django.urls import path
from .views import category_list, category_add, todo, todo_update

urlpatterns = [
    path('categories/', category_list),
    path('categories/add/', category_add),
    path('todo/', todo),
    path('todo/<int:pk>', todo_update)
]