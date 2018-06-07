from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profil



class InscriptionForm(ModelForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})


    class Meta:
        model=User
        fields=['first_name','last_name','email','password']

class ProfilForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].widget.attrs.update({'class': 'form-control'})
        self.fields['language'].widget.attrs.update({'class': 'form-control', 'size': '2'})

    class Meta:
        model=Profil
        fields=['role','language']