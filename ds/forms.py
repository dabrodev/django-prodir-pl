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