from django import forms
from .models import PersonModel, KeywordModel


class PersonForm(forms.ModelForm):
    class Meta:     
        model = PersonModel
        fields = ["username"]

class KeywordForm(forms.ModelForm):
    class Meta:
        model = KeywordModel
        fields = ["keyword"]