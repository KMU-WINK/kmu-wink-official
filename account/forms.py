from django.forms import ModelForm
from .models import User
from django import forms
from captcha.fields import CaptchaField

class DateInput(forms.DateInput):
    input_type = 'date'

class SignUpForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ['email', 'password', 'name', 'student_number', 'date_of_birth', 'graduation_date', 'description', 'github_url', 'website_url', 'profile_thumbnail']
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
            'graduation_date': DateInput(attrs={'type': 'date'}),
            'password': DateInput(attrs={'type': 'password'}),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # 각 input 태그의 help_text, label을 제거함.
        # for field in self.fields:
        #     self.fields[field].help_text = None
        #     self.fields[field].label = ''
        self.fields['description'].widget.attrs['placeholder'] = "조직도에 노출되는 소개글 입니다."
        self.fields['student_number'].widget.attrs['placeholder'] = "ex: 20161313"
