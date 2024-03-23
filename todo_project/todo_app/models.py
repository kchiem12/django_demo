from django.db import models

# Create your models here.

class TodoItem(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title