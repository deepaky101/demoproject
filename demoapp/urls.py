from django.urls import path
from .views import home, form_view

urlpatterns = [
    path('', home, name='home'),
    path('form/', form_view, name='form'),
]
