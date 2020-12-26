from django.contrib import admin

# Register your models here.
#admin.site.register(Profile)
from .models import Profile

admin.site.register(Profile)