
from django.conf.urls import url

from . import views

app_name = 'profiles'
urlpatterns = [
	url(r'^$', views.profile_list, name='list'),
	url(r'^(?P<pk>\d+)/$', views.profile_detail, name='detail'),
	url(r'^(?P<pk>\d+)/edit/$', views.edit_profile, name='edit'),
	url(r'^(?P<pk>\d+)/add_review/$', views.add_review, name='add_review'),
]