from django.contrib import admin
# admin.py

from django.contrib import admin
from .models import CalligraphyStyle, Artwork

admin.site.register(CalligraphyStyle)
admin.site.register(Artwork)

# Register your models here.
