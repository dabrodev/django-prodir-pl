from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context
from django.template.loader import get_template
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .forms import MainContactForm

from profiles.models import Profile

def home(request):
	
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def contact(request):

	form_class = MainContactForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			contact_phone = request.POST.get('contact_phone', '')
			contact_message = request.POST.get('contact_message', '')

			template = get_template('contact_template.txt')
			context = Context({
				'contact_name': contact_name,
				'contact_email': contact_email,
				'contact_phone': contact_phone,
				'contact_message': contact_message,
				})
			content = template.render(context)

			email = EmailMessage(
				"Nowa wiadomość z formularza ZMD",
				content,
				'no-reply@damiandab.com',
				['dabdamian@gmail.com',],
				headers = {'Reply-To': contact_email}
				)
			email.send()
			messages.success(request, 'Wiadomość została wysłana!')
			return redirect('contact')

	
	return render(request, 'contact.html', {'form': form_class})

def policy(request):
	
	return render(request, 'policy.html')

def toc(request):
	
	return render(request, 'toc.html')	


@login_required
def panel(request):
	profile = request.user.profile
	return render(request, 'panel.html', {'user': request.user,'profile': profile,})

