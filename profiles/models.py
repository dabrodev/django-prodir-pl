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
	description = models.TextField(blank=True)
	city = models.CharField(max_length=100, blank=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def get_approved_reviews(self):
		return self.review_set.filter(approved="True")

	def __str__(self):
		return self.user.get_full_name()

class Review(models.Model): 
	profile = models.ForeignKey(Profile)
	pub_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	name = models.CharField(max_length=254)
	email = models.EmailField(max_length=254)
	company = models.CharField(max_length=254, blank=True, null=True)
	position = models.CharField(max_length=254, blank=True, null=True)
	message = models.TextField()
	approved = models.BooleanField(default=False)


def create_profile(sender, **kwargs):
	if kwargs['created']:
		profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
