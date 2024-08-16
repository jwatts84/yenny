from django.urls import path
from . import views

urlpatterns = [
    path('oauth2/start/', views.oauth2_start, name='oauth2_start'),
    path('oauth2/callback/', views.oauth2_callback, name='oauth2_callback'),
    path('create_contact/', views.create_contact, name='create_contact'),
]
