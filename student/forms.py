from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(label='User:', max_length='50', required=True, initial='Enter your name', strip=True)
    user_pwd = forms.CharField(label='Password:', widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    user_name = forms.CharField(label='User:', max_length='50', required=True, initial='Enter your name', strip=True)
    user_pwd = forms.CharField(label='Password:', widget=forms.PasswordInput)
    user_pwd_confirm = forms.CharField(label='Password:', widget=forms.PasswordInput)