from django.db import models
from django.contrib.auth.models import User

# Status Choices
STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
]

# Category Choices
CATEGORY_CHOICES = [
    ('Work', 'Work'),
    ('Personal', 'Personal'),
    ('Other', 'Other'),
]

# Priority Choices
PRIORITY_CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
]

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    
    tags = models.CharField(max_length=100, blank=True, help_text="Comma-separated tags (e.g. Django, Resume)")
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title