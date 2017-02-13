from django.forms import ModelForm

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

	def clean_image(self):
		image = self.cleaned_data.get('avatar',False)
		if image:
		 if image._size > 1*512*512:
		       raise ValidationError("Image file too large ( > 0.5mb )")
		 return image
		else:
		 raise ValidationError("Couldn't read uploaded image")


class AccountForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','password')