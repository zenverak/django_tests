from django import forms
from .models import Child, Parent
from django.contrib.auth.models import User

class AuthenticationForm(forms.Form):

    username = forms.CharField(max_length=25,label="UserName")
    password = forms.CharField(widget=forms.PasswordInput())




class SignUp(forms.Form):
    email = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('email', 'username', 'password',)


class PersonAdd(forms.Form):

    class Meta:
        fields = ('first_name', 'middle_name', 'last_name', 'dob', 'address')

class ParentAddForm(PersonAdd):
    
    class Meta(PersonAdd.Meta):
        model = Parent


class ChildAddForm(PersonAdd):

    parent = forms.ModelChoiceField(queryset=Parent.objects.all())
    class Meta(PersonAdd.Meta):
        model = Child
        fields = PersonAdd.Meta.fields + ('school',)
