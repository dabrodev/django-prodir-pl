from django.forms import ModelForm, TextInput
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from .models import Profile

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ('avatar', 'description','city', )

		labels = {
            "description": "Opis",
            "city": "Miasto",
        }


class AccountForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','password')

		widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Imie'}),
        }