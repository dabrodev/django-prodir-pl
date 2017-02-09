from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from .models import Profile
from .forms import ProfileForm

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

	form_class = ProfileForm
    
	if request.method == 'POST':

	    form = form_class(data=request.POST, instance=profile)
	    
	    if form.is_valid():
	    	form.save()
	    	return redirect('profiles:detail', pk=profile.pk)
	else:
	    form = form_class(instance=profile)
	return render(request, 'profiles/edit_profile.html', {'profile': profile, 'form': form,})