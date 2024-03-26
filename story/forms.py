from django import forms
from story.model import *

class cform(forms.ModelForm):
    class Meta:
        model= customer
        fields="__all__"