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
        'placeholder': 'Enter your name'
    }))

class RegisterForm(forms.Form):
    user_name = forms.CharField(label='User:', max_length='50', required=True, strip=True,
    widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your name'
    })
    )
    user_pwd = forms.CharField(label='Password:', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password'
    }))
    user_pwd_confirm = forms.CharField(label='Password:', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Repeat your password'
    }))

class EditForm(forms.Form):
    stu_name = forms.CharField(label='姓名:', max_length='20', required=True, strip=True,
    widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '输入姓名'
    })
    )
    stu_id = forms.CharField(label='身份证号：:'
                             , max_length='18', required=True, strip=True,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': '输入身份证号'
                             })
                             )
    stu_sex = forms.BooleanField(label='性别', required=True)
    stu_birth = forms.DateField(label='出生日期:', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'placeholder': '年-月-日'
    }))


c