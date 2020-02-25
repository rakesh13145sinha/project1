from django import forms
from accounts.models import Profiles,Driver
class Profileform(forms.ModelForm):
    class Meta:
        model=Profiles
        fields='__all__'
class DriverForm(forms.ModelForm):
    class Meta:
        model=Driver
        fields=('first_name','last_name','mobile','car','license_no','ownership_no')