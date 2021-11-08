from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module
#extra : Allows you to set the number of empty extra forms to display in the formset
ModuleFormSet = inlineformset_factory(Course, Module, fields=['title','description'], extra = 2, can_delete=True)
