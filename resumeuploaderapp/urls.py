from django.urls import path
from . import views

urlpatterns = [
    path('post/',views.ProfileView.as_view(),name='post'),
    path('get/',views.ProfileView.as_view(),name='get')
]
