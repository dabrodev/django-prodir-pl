from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from profiles.models import Profile

def home(request):
	
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	
	return render(request, 'contact.html')

def priv_policy(request):
	
	return render(request, 'privacy-policy.html')

def toc(request):
	
	return render(request, 'toc.html')	


@login_required
def panel(request):
	profile = request.user.profile
	return render(request, 'panel.html', {'user': request.user,'profile': profile,})

