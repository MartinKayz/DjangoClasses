from django import forms
from rentme.models import Student

class myform(forms.ModelForm):
    class Meta:
        model = Student
        fields ="__all__"