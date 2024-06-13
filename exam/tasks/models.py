from django.db import models

# Create your models here.

class Tasks(models.Model):
    task_id = models.IntegerField()
    task_name = models.CharField(max_length=255)
    task_description = models.TextField()
    create_at= models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

class SubTasks(models.Model):
    subtask_id = models.IntegerField()
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='subtasks')
    subtask_name = models.CharField(max_length=255)
    subtask_description = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
