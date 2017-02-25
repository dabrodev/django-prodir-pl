
from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView

from . import views

app_name = 'profiles'
urlpatterns = [
	url(r'^$', views.profile_list, name='list'),
	url(r'^kontakt-doradca/$', views.message_to_consultant, name='ask_consultant'),
	url(r'^(?P<pk>\d+)/$', views.profile_detail, name='detail'),
	url(r'^(?P<pk>\d+)/edit/$', views.edit_profile, name='edit'),
	url(r'^(?P<pk>\d+)/opinia/$', views.add_review, name='add_review'),
	url(r'^(?P<pk>\d+)/kontakt-doradca/$', views.inquiry, name='inquiry'),
	url(r'^\d+/password/$', RedirectView.as_view(pattern_name='account_change_password', permanent=False))
]