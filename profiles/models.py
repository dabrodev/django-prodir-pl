from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError

# Create your models here.

class Profile(models.Model):

	def validate_image(fieldfile_obj):
		filesize = fieldfile_obj.file.size
		megabyte_limit = 1
		if filesize > megabyte_limit*1024*1024:
			raise ValidationError("Zbyt duży rozmiar pliku. Użyj zdjęcia o rozmiarze poniżej %sMB" % str(megabyte_limit))

	user = models.OneToOneField(User, blank=True, null=True)
	avatar = models.ImageField(upload_to='avatar', blank=True, validators=[validate_image])
	description = models.TextField()
	city = models.CharField(max_length=100)

	def __str__(self):
		return self.user.get_full_name()

class Review(models.Model): 
	pass		

def create_profile(sender, **kwargs):
	if kwargs['created']:
		profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
