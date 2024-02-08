from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views  # Import the auth views

from . import views

app_name = 'djangoapp'
urlpatterns = [
    path('signup/', views.signup, name='signup'),  # Correct URL pattern for signup view
    path('', views.get_dealerships, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # Add URL patterns for login, logout, and signup views
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
