from django.db import models

class Task(models.Model):
    task_text = models.CharField(max_length=200)
