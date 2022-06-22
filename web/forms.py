from django import forms
from .models import Contact
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'name':TextInput(attrs={'placeholder':"Your Name",'name':"name",'class':" required form-control"}),
            'email':EmailInput(attrs={'placeholder':"Your Email",'name':"email",'class':"required form-control"}),
            'phone':TextInput(attrs={'placeholder':"Your Phone",'name':"phone",'class':"required form-control"}),
            'subject':TextInput(attrs={'placeholder':"Subject",'name':"address",'class':"form-control"}),
            'message':Textarea(attrs={'placeholder':"Comment",'name':"message",'class':"form-control",'rows':"6"}),
         }