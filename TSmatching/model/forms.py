from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(label='Username:',
                                max_length='50',
                                required=True, strip=True,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control input-box',
                                    'placeholder': 'Enter your name'
                                }))
    user_pwd = forms.CharField(label='Password:', widget=forms.PasswordInput(attrs={
        'class': 'form-control input-box',
        'placeholder': 'Enter your password'
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
    user_pwd_confirm = forms.CharField(label='Confirm your password :', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Repeat your password'
    }))
    user_email = forms.CharField(label='Email:', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email address'
    }))
    verification_code = forms.CharField(label='Verification Code', max_length=4, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Characters Below'
    }))

class PasswordChangeForm(forms.Form):
    user_pwd = forms.CharField(label='Password:', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password'
    }))
    user_pwd_confirm = forms.CharField(label='Confirm your password :', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Repeat your password'
    }))

class EditForm(forms.Form):
    stu_name = forms.CharField(label='姓名:', max_length='20', required=True, strip=True,
    widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '输入姓名',
    })
    )
    stu_id = forms.CharField(label='身份证号：'
                             , max_length='18', required=True, strip=True,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': '输入身份证号'
                             })
                             )
    stu_sex = forms.ChoiceField(label='性别:', required=True, widget=forms.Select(attrs={
        'class':'form-control'
    }),
                                choices=(('1', '男',), ('0', '女',)))
    stu_birth = forms.DateField(label='出生日期:', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'placeholder': '年-月-日'
    }))
    stu_email = forms.EmailField(label='电子邮箱：',
                                 widget=forms.EmailInput(attrs={'class':'form-control',
                                                                'placeholder':'邮箱'}))
    stu_phone_number = forms.CharField(label='手机号：',max_length=25, required=True,
                                       widget=forms.TextInput(attrs={'class':'form-control',
                                                                     'placeholder':'手机号码'}))
    stu_university = forms.CharField(label='本科学校：',max_length=25, required=True,
                                     widget=forms.TextInput(attrs={'class':'form-control',
                                                                   'placeholder':'本科学校名称'}))
    stu_major = forms.CharField(label='本科专业：', required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': '填写本科专业名称'}))
    stu_gpa = forms.CharField(label='学分绩：', required=True,
                              widget=forms.TextInput(attrs={'class':'form-control',
                                                            'placeholder':'百分制，如没有，使用4分制GPA'}))
    stu_ranking = forms.CharField(label='专业排名（百分比）：', required=True,
                                  widget=forms.TextInput(attrs={
                                      'class':'form-control',
                                      'placeholder':'专业排名百分比'
                                  }))
    stu_comment = forms.CharField(label='备注（可选）', required=False,
                                    widget=forms.TextInput(attrs={
                                      'class':'form-control',
                                      'placeholder':'如有其他信息请备注'
                                  }))
    stu_attachment = forms.FileField(required=False)
    stu_pic = forms.FileField()