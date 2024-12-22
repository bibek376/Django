from crud_app.models import Info_Model
from django import forms 


class Info_Form(forms.ModelForm):
    class Meta:
        model = Info_Model
        fields = ['title', 'description']
