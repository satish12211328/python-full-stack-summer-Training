from django.urls import path


from todolist.views import TodoDeleteView, TodoListView, TodoCreateView, TodoUpdateView

urlpatterns =[
    path('', TodoListView.as_view(),name="todo_view"),
    path('create/', TodoCreateView.as_view(),name="todo_create"),
    path('update/<int:pk>/', TodoUpdateView.as_view(),name="todo_update"),
    path('delete/', TodoDeleteView.as_view(),name="todo_delete"),
]