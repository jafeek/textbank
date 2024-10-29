from django import forms
from .models import Reform,Register,Login
class Regform(forms.ModelForm):
    class Meta :
        model = Reform
        fields = "__all__"
        widgets ={}

class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields="__all__"
        widgets={ }
class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields="__all__"
        widgets={ }