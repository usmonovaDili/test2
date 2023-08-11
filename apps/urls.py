from django.urls import path
from .views import AllTodosView, CreateToDoViews, AllToDoViews, DeleteTodoViews, UpdateToDoViews, ToDoQueryViews

urlpatterns = [
    path('all/', AllTodosView.as_view()),
    path('', AllToDoViews.as_view()),
    path('create/', CreateToDoViews.as_view()),
    path('update/', UpdateToDoViews.as_view()),
    path('delete/', DeleteTodoViews.as_view()),
    path('search/', ToDoQueryViews.as_view())
]
