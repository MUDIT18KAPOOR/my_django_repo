from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != "z":
        raise forms.ValidationError("Name Needs to Start with z only !")




class basic(forms.Form):
    FirstName = forms.CharField(max_length=100, validators=[check_for_z])
    LastName = forms.CharField(max_length=100)
    Email = forms.EmailField()
    verify_email= forms.EmailField(label="ReEnter Your Email Here : ")
    Text = forms.CharField(widget=forms.Textarea)
    botcatcher= forms.CharField(required=False ,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

def clean(self):
     all_clean_data = super().clean()
     email= all_clean_data["email"]
     vmail = all_clean_data["verify_email"]

     if email != vmail:
         raise forms.ValidationError("Emails Missmatch")


    # def clean_botcatcher(self):
    #  botcatcher= self.cleaned_data["botcatcher"]
    #  if len(botcatcher) > 0:
    #     raise forms.ValidationError("Error Bot Interuption")
    #  return botcatcher

