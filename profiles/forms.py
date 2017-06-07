from django import forms
from django.forms import ModelForm, TextInput
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from .models import Profile, Review, Inquiry

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

class InquiryForm(ModelForm):
	class Meta:
		model = Inquiry
		fields = ('name', 'email', 'tel', 'message')

		labels = {
			'name': 'Imię i Nazwisko',
			'email': 'E-Mail',
			'tel': 'Telefon',
			'message': 'Wiadomość',
		}


class AccountForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('first_name','last_name', 'password')

		widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Imię'}),
        }


class MessageForm(forms.Form):
	user = User.objects.all()

	client = forms.CharField(
		label=_("Twoje imię i nazwisko"),
		widget=forms.TextInput,
		required=True,
	)
	email = forms.EmailField(
		label=_("Email kontaktowy"),
		
		required=True,
	)
	tel = forms.CharField(
		label=_("Telefon"),
		widget=forms.TextInput,
		required=False,
	)
	recipient = forms.ModelChoiceField(
		label=_("Wybierz doradcę nieruchomości"),
		queryset=Profile.objects.filter(city__gt='', description__gt=''),
		required=False,
	)
	message = forms.CharField(
		label=_("Wiadomość"),
		widget=forms.Textarea,
		required=True,
	)

	def __init__(self, request, *args, **kwargs):
		super(MessageForm, self).__init__(*args, **kwargs)
		self.request = request
		self.fields["recipient"].queryset = \
			self.fields["recipient"].queryset.\
			exclude(pk=request.user.pk)

	def save(self):
		cleaned_data = self.cleaned_data
		send_mail(
			subject=ugettext("A message from %s") % \
				'ZnajdźMiDom',
			message=cleaned_data["message"],
			from_email='no-reply@znajdzmidom.pl',
			recipient_list=[
				'dabdamian@gmail.com',
			],
			fail_silently=True,
		)