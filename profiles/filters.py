from django.contrib.auth.models import User

import django_filters
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, MultiField

from .models import Profile


class ProfileFilter(django_filters.FilterSet):
	user__first_name = django_filters.CharFilter(label='Imię', lookup_expr='icontains')
	user__last_name = django_filters.CharFilter(label='Nazwisko', lookup_expr='icontains')
	city = django_filters.CharFilter(label='Miasto', lookup_expr='icontains')

	class Meta:
		model = Profile
		fields = ['user__first_name', 'user__last_name', 'city']
		labels = {
			'user__first_name': 'Imię',
			'user__last_name': 'Nazwisko',
			'city': 'Miasto',
		}
	