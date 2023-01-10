from django import forms
from django.forms import ModelForm
from dr_shahida.models import  Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
