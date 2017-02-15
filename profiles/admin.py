from django.contrib import admin
from django.contrib.auth.models import User

from .models import Profile, Review

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	model = Profile
	list_display = ('full_name', 'city','timestamp', 'updated')
	list_filter = ['timestamp', 'updated']

	def full_name(self, obj):
		
		return obj.user.get_full_name()

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('profile', 'name', 'message', 'pub_date', 'approved')
    list_filter = ['pub_date']
    search_fields = ['message']

admin.site.register(Profile, ProfileAdmin)    
admin.site.register(Review, ReviewAdmin) 