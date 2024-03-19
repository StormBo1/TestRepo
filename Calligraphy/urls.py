from django.urls import path
from django.contrib.auth import views as auth_views
from .views import display_screen, about_calligraphy, styles_list, artwork_list, signup_view, authenticate_user, landing_page
# from . import views


app_name = 'Calligraphy'


urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('authenticate_user/', authenticate_user, name='authenticate_user'),
    path('signup/', signup_view, name='signup'),
    path('display/', display_screen, name='display_screen'),
    path('about/', about_calligraphy, name='about_calligraphy'),
    path('styles/', styles_list, name='styles_list'),
    path('artworks/', artwork_list, name='artwork_list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]