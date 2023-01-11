from .models import*
from django import forms

class ClientNewsCreateForm(forms.ModelForm):
    class Meta:
        model= News
        fields="__all__"
        widgets={
            'title': forms.TextInput(),
            'category': forms.Select(),
            'content': forms.Textarea(),
            'image': forms.ClearableFileInput(),
        }
        
class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "username...",
    }))
    password= forms.CharField(widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder' : "Enter your password..."
    }))