from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, blank=True, null=True)
	description = models.TextField()
	city = models.CharField(max_length=100)

	def __str__(self):
		return self.user.get_full_name()

def create_profile(sender, **kwargs):
	if kwargs['created']:
		profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
