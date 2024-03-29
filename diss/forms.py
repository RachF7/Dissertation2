from django import forms
from django.forms import ModelForm

from diss.models import UserProfile, forum, Discussion

from django.contrib.auth.models import User


# Create your forms here.
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)


class CreateInForum(ModelForm):
    class Meta:
        model = forum
        fields = "__all__"


class CreateInDiscussion(ModelForm):
    class Meta:
        model = Discussion
        fields = "__all__"