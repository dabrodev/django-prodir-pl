from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from .models import Profile, Review
from .forms import ProfileForm, ReviewForm

# Create your views here.
def profile_list(request):
	profiles = Profile.objects.all()
	return render(request, 'profiles/profile_list.html', {
		'profiles': profiles, 
		})

def profile_detail(request, pk):
	profile = get_object_or_404(Profile, pk=pk)
	return render(request, 'profiles/profile_detail.html', {'profile': profile})

@login_required
def edit_profile(request, pk):
	
	profile = Profile.objects.get(pk=pk)

	if profile.user != request.user:
		raise Http404

	if request.method == 'POST':

	    form = ProfileForm(request.POST, request.FILES, instance=profile)
	    
	    if form.is_valid():
	    	form.save()
	    	messages.success(request, 'Profil zaktualizowany')
	    	return redirect('profiles:detail', pk=profile.pk)
	else:
	    form = ProfileForm(instance=profile)
	return render(request, 'profiles/edit_profile.html', {'profile': profile, 'form': form,})

def add_review(request, pk):
	profile = get_object_or_404(Profile, pk=pk)

	if request.method == 'POST':

		form = ReviewForm(request.POST, instance=profile)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			company = form.cleaned_data['company']
			position = form.cleaned_data['position']
			message = form.cleaned_data['message']

			review = Review()
			review.profile = profile
			review.name = name
			review.email = email
			review.company = company
			review.position = position
			review.message = message

			review.save()
			messages.success(request, 'Opinia dodana. Pojawi się na profilu po zatwierdzeniu przez administratora.')
			# Always return an HttpResponseRedirect after successfully dealing
			# with POST data. This prevents data from being posted twice if a
			# user hits the Back button.
			return redirect('profiles:detail', pk=profile.pk)

	else:
		form = ReviewForm(instance=profile)         

	return render(request, 'profiles/review.html', {'profile': profile, 'form': form})	
