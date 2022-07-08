from django.forms import ModelForm, widgets
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class':'input form-control', 'placeholder':'Add Title'}),
            'description':forms.Textarea(attrs={'class':'input form-control', 'placeholder':'Add Description'}),
            'tags':forms.SelectMultiple(attrs={'class':'form-select'}),
            'owner':forms.Select(attrs={'class':'form-select'}),
            'featured_image':forms.FileInput(attrs={'class':'form-control form-control-lg'}), #form-control form-control-lg
            'demo_link':forms.TextInput(attrs={'class':'input form-control', 'placeholder':'Add Demo Link'}),
            'source_code':forms.TextInput(attrs={'class':'input form-control', 'placeholder':'Add Source Link'}),
        }

        # def __init__(self, *args, **kwargs):
        #     super(ProjectForm, self).__init__(*args, **kwargs)

        #     self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Add Text'})