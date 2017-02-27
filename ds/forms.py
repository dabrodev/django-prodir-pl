from django import forms

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='Imię',
    	widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    last_name = forms.CharField(max_length=30, label='Nazwisko',
    	widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

class ContactForm(forms.Form):

	client = forms.CharField(
		label= "Twoje imię i nazwisko",
		widget=forms.TextInput,
		required=True,
	)
	email = forms.EmailField(
		label="Email kontaktowy",
		
		required=True,
	)
	tel = forms.CharField(
		label="Telefon",
		widget=forms.TextInput,
		required=False,
	)

	message = forms.CharField(
		label="Wiadomość",
		widget=forms.Textarea,
		required=True,
	)

		

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

class MainContactForm(forms.Form):
    contact_name = forms.CharField(label= "Imię i nazwisko")
    contact_email = forms.EmailField(label="E-Mail")
    contact_phone = forms.CharField(required=False, label= "Telefon")
    contact_message = forms.CharField(label= "Wiadomość", widget=forms.Textarea)

