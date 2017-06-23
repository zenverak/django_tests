from django import forms
from .models import Child, Parent
from django.contrib.auth.models import User

class AuthenticationForm(forms.Form):

    username = forms.CharField(max_length=25,label="UserName")
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fiels = ['username', 'password']


class SignUp(forms.Form):

    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class PersonAdd(forms.Form):

    class Meta:
        fields = ('first_name', 'middle_name', 'last_name', 'dob', 'address')

class ParentAdd(PersonAdd):
    
    class Meta(PersonAdd.Meta):
        model = Parent


class ChildAdd(PersonAdd):

    parent = forms.ModelChoiceField(queryset=Parent.objects.all())
    class Meta(PersonAdd.Meta):
        model = Child
        fields = PersonAdd.Meta.fields + ('school',)
