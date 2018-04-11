from django.urls import include, path
from . import views as core_views

urlpatterns = [
    path('', core_views.snake_list, name='snake'),
    path('create', core_views.snake_create, name='snake_create'),
    path('<int:snake_id>', core_views.snake_edit, name='snake_edit'),
]