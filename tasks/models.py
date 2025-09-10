from django.db import models
from authentication.models import User


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('working', 'Working'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    additional_info = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='admin_user', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='employee_user', null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
