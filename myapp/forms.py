from django import forms
from django.forms import ModelForm
from .models import Task,Dear
from django.core import validators
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

	class Meta:
		model = Task
		fields ='__all__'

class DearForm(forms.ModelForm):
	note = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'add dairy.......'}))

	class Meta:
		model = Dear
		fields = '__all__'



