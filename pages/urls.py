from django.urls import path
from .views import home_page_view

urlpatterns = [
    path('', home_page_view, name='home'), # Forwarding the home page from project level urls.py to app level urls.py
]
