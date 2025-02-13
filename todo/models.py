from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


class Todo(models.Model):
    PRIORITY_SELECT = [
        ('l', 'Low'),
        ('m', 'Medium'),
        ('h', 'High'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_SELECT, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Todo, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('todo:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def get_update_url(self):
        return reverse('todo:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('todo:delete', args=[self.pk])

    @property
    def status_display(self):
        return "Active" if not self.completed else "Completed"

    @property
    def status_class(self):
        return "bg-green-200 text-green-700" if self.completed else "bg-red-200 text-red-700"

    def __str__(self):
        return f"{self.title}"
