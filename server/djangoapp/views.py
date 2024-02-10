from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from .restapis import get_dealers_from_cf, get_dealer_reviews_from_cf
from django.http import HttpResponse

# Define your views here

def registration_view(request):
    # Your registration logic here
    return HttpResponse("Registration view")

def get_dealer_details(request, dealer_id):
    url = "https://example.com/get-reviews"  # Replace with your actual URL
    reviews = get_dealer_reviews_from_cf(url, dealer_id)
    context = {'reviews': reviews}
    return HttpResponse("Dealer Reviews: {}".format(reviews))


def view1(request):
    # Function body for view1
    return HttpResponse("View 1")

def view2(request):
    # Function body for view2
    return HttpResponse("View 2")

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Log in the user after successful sign-up
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'You have been successfully registered and logged in!')
            return redirect('djangoapp:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'djangoapp/signup.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out!')
    return redirect('djangoapp:index')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have been successfully logged in!')
            return redirect('djangoapp:index')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'djangoapp/login.html', {'form': form})

def about(request):
    return render(request, 'djangoapp/about.html')

def contact(request):
    return render(request, 'djangoapp/contact.html')

def get_dealerships(request):
    if request.method == "GET":
        context = {}
        url = "https://favouralain-3000.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/dealerships/get"
        dealerships = get_dealers_from_cf(url)
        context["dealership_list"] = dealerships
        return render(request, 'djangoapp/index.html', context)
