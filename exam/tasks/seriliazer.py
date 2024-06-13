from rest_framework import serializers
from .models import Tasks, SubTasks

class TasksSeriliazer(serializers.ModelSerializer):
    class Meta:
        model=Tasks
        fields = "__all__"

class subtasks_seriliazer(serializers.ModelSerializer):
    class Meta:
        model = SubTasks
        fields = '__all__'