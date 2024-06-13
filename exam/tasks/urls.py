from django.urls import path
from .views import TasksCreateView,TasksGetAll,DeleteTask,UpdateTasks,SubTaskCreate,filter_by_taskId

urlpatterns = [
    path('',TasksGetAll.as_view()),
    path('createTask',TasksCreateView.as_view()),
    path('taskDelete/<int:pk>',DeleteTask.as_view()),
    path('taskUpdate/<int:pk>',UpdateTasks.as_view()),
    path('createSubTask',SubTaskCreate.as_view()),
    path('get_filter_task_id/',filter_by_taskId.as_view())
]