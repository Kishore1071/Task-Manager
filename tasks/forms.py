from django import forms
from .models import Task
from authentication.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            # 'status': forms.Select(attrs={'class': 'form-select'}),
            # 'additional_info': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'assigned_to': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.fields['assigned_to'].queryset = User.objects.filter(role='employee')
