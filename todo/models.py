from django.db import models
from django.shortcuts import reverse


class Todo(models.Model):
    PRIORITY_SELECT = [
        ('l', 'Low'),
        ('m', 'Medium'),
        ('h', 'High'),
    ]

    STATUS_CHOICES = [
        ('ac', 'Active'),
        ('com', 'Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=1, choices=PRIORITY_SELECT, blank=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='ac')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def get_detail_url(self):
        return reverse('todo:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('todo:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('todo:delete', args=[self.pk])

    def toggle_status(self):
        self.status = 'completed' if self.status == 'ac' else 'ac'
        self.save()

    def __str__(self):
        return f"{self.title}"
