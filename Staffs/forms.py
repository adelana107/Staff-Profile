from django import forms
from .models import Staffs_profile


class Staffsform(forms.ModelForm):
    class Meta:
        model = Staffs_profile
        fields = ['name', 'mobile', 'levels', 'qualifications', 'experience', 'marital_status' ]