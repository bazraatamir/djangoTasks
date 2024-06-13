from django.shortcuts import render
from rest_framework import generics
from .models import Tasks,SubTasks
from .seriliazer import TasksSeriliazer,subtasks_seriliazer

# Create your views here.

class TasksCreateView(generics.CreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSeriliazer

class TasksGetAll(generics.ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSeriliazer

class DeleteTask(generics.DestroyAPIView):
    queryset= Tasks.objects.all()
    serializer_class = TasksSeriliazer

class UpdateTasks(generics.UpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSeriliazer

class SubTaskCreate(generics.CreateAPIView):
    queryset = SubTasks.objects.all()
    serializer_class= subtasks_seriliazer

class filter_by_taskId(generics.ListAPIView):
    serializer_class = subtasks_seriliazer
    def get_queryset(self):
        queryset = SubTasks.objects.all()
        task_id = self.request.query_params.get('task_id')
        if( task_id is not None):
            queryset = queryset.filter(task_id=task_id)
        return queryset