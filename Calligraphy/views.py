from .models import CalligraphyStyle, Artwork  # might be an issue here. CalligraphyStyle is it being used?
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
# views.py


def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(
            reverse('Calligraphy:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('Calligraphy:display_screen')
        )

# Sign up new users
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('Calligraphy:display_screen'))  # Replace 'home' with the name of your home page URL
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# upon successful login user will be redirected to display_screen (home page)
@login_required     # this is my show user example
def display_screen(request):
    context = {'user': request.user}
    return render(request, 'Calligraphy/displayScreen.html', context)


def landing_page(request):
    return render(request, 'Calligraphy/landing_page.html')

# about calligrpahy page
def about_calligraphy(request):
    context = {}
    return render(request, 'Calligraphy/about_calligraphy.html', context)

# style page
def styles_list(request):
    #context = {}
    styles = CalligraphyStyle.objects.all()
    return render(request, 'Calligraphy/styles_list.html',{'styles': styles}) #context)

# types of artwork page
def artwork_list(request): #style_id=None):
    context={}
    return render(request, 'Calligraphy/artwork_list.html', context)#{'artworks': artworks})

# logout option
def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    # Logout logic here if needed
    return render(request, 'logout.html')
# Create your views here.
