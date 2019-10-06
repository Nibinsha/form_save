from django import forms

from .models import User, Task


class loginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'passwod',)


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'date',)