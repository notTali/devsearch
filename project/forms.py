from django.forms import ModelForm, widgets
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add Title'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Add Description'}),
            'tags':forms.SelectMultiple(attrs={'class':'form-select'}),
            'owner':forms.Select(attrs={'class':'form-select'}),
            'demo_link':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add Demo Link'}),
            'source_code':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add Source Link'}),
        }

        