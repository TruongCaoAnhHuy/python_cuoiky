from django import forms
# creating a form
class LoginForm(forms.Form):
    user_name = forms.CharField(label='', max_length = 100, widget=forms.TextInput(attrs={'class':'box', 'placeholder' : 'User name'}))
    password = forms.CharField(label='', widget = forms.PasswordInput(attrs={'class':'box', 'placeholder' : 'Password'}))

class RegisterForm(forms.Form):
    user_name = forms.CharField(label='', max_length = 100, widget=forms.TextInput(attrs={'class':'box', 'placeholder' : 'User name'}))
    password = forms.CharField(label='', widget = forms.PasswordInput(attrs={'class':'box', 'placeholder' : 'Password'}))
    c_password = forms.CharField(label='', widget = forms.PasswordInput(attrs={'class':'box', 'placeholder' : 'Confirm Password'}))