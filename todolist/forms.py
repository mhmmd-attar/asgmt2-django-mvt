from django import forms
from todolist.models import Task

class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
