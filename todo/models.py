from django.db import models


class Todo(models.Model):
    PRIORITY_SELECT = [
        ('l', 'Low'),
        ('m', 'Medium'),
        ('h', 'High'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=2, choices=PRIORITY_SELECT, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)



    def __str__(self):
        return f"{self.title}"
