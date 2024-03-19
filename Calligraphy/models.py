from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CalligraphyStyle(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField()


class Artwork(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    style = models.ForeignKey(CalligraphyStyle, on_delete=models.CASCADE)
    artist = models.CharField(max_length=100)
    image = models.ImageField(upload_to='artwork_images/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)


def __str__(self):
    return self.title
# Create your models here.
