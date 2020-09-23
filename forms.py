from django import forms
from django.contrib.auth.models import User,auth

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',                
        ]
class LoginForm(forms.Form):
      username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter UserName'}))
      password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
      class Meta:
          fields = [
            'username',
            'password'
          ]
      def clean(self,*args,**kwargs):
          username = self.cleaned_data.get('username')
          password = self.cleaned_data.get('password')    