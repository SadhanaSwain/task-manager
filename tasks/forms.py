from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'status', 'priority', 'due_date', 'tags']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'title': 'Task Title',
            'description': 'Details',
            'category': 'Task Category',
            'status': 'Current Status',
            'priority': 'Priority Level',
            'tags': 'Tags (comma-separated)',
            'due_date': 'Due Date',
        }

    def _init_(self, *args, **kwargs):
        super(TaskForm, self)._init_(*args, **kwargs)
        # Set initial value for priority to 'Medium'
        self.fields['priority'].initial = 'Medium'