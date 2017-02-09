from django.forms import ModelForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from .models import Profile

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ('description',)


class AccountForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','password')