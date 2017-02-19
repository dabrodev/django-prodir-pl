from django.forms import ModelForm, TextInput
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from .models import Profile, Review

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ('avatar', 'description','city')

		labels = {
            'description': 'Opis',
            'city': 'Miasto',
        }

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ('name', 'email', 'company', 'position', 'message')

		labels = {
			'name': 'Imię i Nazwisko',
			'email': 'E-Mail',
			'company': 'Firma',
			'position': 'Rola w firmie',
			'message': 'Opinia',

		}



class AccountForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','email', 'password')

		widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Imię'}),
        }