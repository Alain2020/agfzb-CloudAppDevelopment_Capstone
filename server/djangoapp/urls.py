# urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Other URL patterns...
    path('registration/', views.registration_request, name='registration_request'),
    # Other URL patterns..
    path('login/', auth_views.LoginView.as_view(template_name='djangoapp/login.html'), name='login'),
    path('', view=views.get_dealerships, name='index'),
    path('about/', view=views.about, name='about'),
    path('contact/', view=views.contact, name='contact'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', view=views.registration_request, name='registration'),
    path('signup/', view=views.signup, name='signup'),  # Add this line for signup view
    path('dealer/<int:dealer_id>/', view=views.get_dealer_details, name='dealer_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
