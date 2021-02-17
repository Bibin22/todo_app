from django.db import models

# Create your models here.
class Tasks(models.Model):
    task_name = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.task_name