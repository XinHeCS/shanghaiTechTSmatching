from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length='50',
                                required=True, strip=True,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter your name'
                                }))
    user_pwd = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password'
    }))