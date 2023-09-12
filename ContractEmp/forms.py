from django import forms
from .models import Contractemployee

class Contractemployee(forms.ModelForm):
    class Meta:
        model = Contractemployee
        fields = '__all__'  # You can replace this with a list of specific fields you want