from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User

from .models import Profile, Review, Inquiry
from .forms import ProfileForm, AccountForm, ReviewForm, InquiryForm, MessageForm
from .filters import ProfileFilter

# Create your views here.
def profile_list(request):
	profile_list = Profile.objects.filter(city__gt='', description__gt='').order_by('?')
	profile_filter = ProfileFilter(request.GET, queryset=profile_list)
	return render(request, 'profiles/profile_list.html', {'filter': profile_filter})

def profile_detail(request, pk):
	profile = get_object_or_404(Profile, pk=pk)
	return render(request, 'profiles/profile_detail.html', {'profile': profile,})

@login_required
def edit_profile(request, pk):
	
	profile = Profile.objects.get(pk=pk)
	user = request.user

	if profile.user != request.user:
		raise Http404

	if request.method == 'POST':

	    p = ProfileForm(request.POST, request.FILES, instance=profile)
	    u = AccountForm(request.POST, instance=user )
	    
	    if p.is_valid() and u.is_valid():
	    	p.save()
	    	u.save()
	    	messages.success(request, 'Profil zaktualizowany')
	    	return redirect('profiles:detail', pk=profile.pk)
	else:
	    p = ProfileForm(instance=profile)
	    u = AccountForm(instance=user)
	return render(request, 'profiles/edit_profile.html', {'profile': profile, 'form_profile': p, 'form_user': u})

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
			send_mail(
			subject="Nowa opinia na %s" % \
				'Idealny Pośrednik',
			message=company,
			from_email='biuro@idealnyposrednik.pl',
			recipient_list=[
				profile.user.email,
			],
			fail_silently=True,
		)

			# Always return an HttpResponseRedirect after successfully dealing
			# with POST data. This prevents data from being posted twice if a
			# user hits the Back button.
			return redirect('profiles:detail', pk=profile.pk)

	else:
		form = ReviewForm(instance=profile)         

	return render(request, 'profiles/review.html', {'profile': profile, 'form': form})

def inquiry(request, pk):
	profile = get_object_or_404(Profile, pk=pk)

	if request.method == 'POST':

		form = InquiryForm(request.POST, instance=profile)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			tel = form.cleaned_data['tel']
			message = form.cleaned_data['message']

			inquiry = Inquiry()
			inquiry.profile = profile
			inquiry.name = name
			inquiry.email = email
			inquiry.tel = tel
			inquiry.message = message

			inquiry.save()
			messages.success(request, 'Wiadomość została wysłana, wkrótce odezwie się doradca.')
			send_mail(
			subject="Nowa wiadomość na %s" % \
				'ZnajdźMiDom',
			message="Zaloguj się na ZnajdzMiDom, aby odczytać wiadomość, i otrzymać dane potencjalnego klienta.",
			from_email='no-reply@znajdzmidom.pl',
			recipient_list=[
				profile.user.email,
			],
			fail_silently=True,
		)

			# Always return an HttpResponseRedirect after successfully dealing
			# with POST data. This prevents data from being posted twice if a
			# user hits the Back button.
			return redirect('profiles:detail', pk=profile.pk)

	else:
		form = InquiryForm(instance=profile)         

	return render(request, 'profiles/inquiry.html', {'profile': profile, 'form': form})	


def message_to_consultant(request):
   if request.method == "POST":
       form = MessageForm(request, data=request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, 'Wiadomość wysłana')
           return redirect('profiles:list')
   else:
       form = MessageForm(request)

   return render(request, "profiles/contact_consultant.html", {"form": form}
   )