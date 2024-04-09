from django.urls import path

from .views import registration_view, profile_view, verification_view

urlpatterns = [
    path('', registration_view, name='registration'),
    path('profile/', profile_view, name='profile'),
    path('verification/', verification_view, name='verification'),
]