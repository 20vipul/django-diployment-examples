# Import necessary modules.
from django.shortcuts import render
from Basic_App.forms import UserForm,UserProfileForm

# Import necessary Modules for Login And Logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

# Define the 'index' view function.
def index(request):
    
    return render(request,"Basic_App/index.html")

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

# Logout view
@login_required #checks wheather any one is avtuallu loged in or not 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Define the 'register' view function for user registration.
def register(request):
    
    # Initialize the 'registered' variable to False.
    registerd = False
    # Check if the request method is POST (form submission).
    if request.method =="POST":
        # Create UserForm and UserProfileForm instances with data from the POST request.
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)
    
        # Check if both forms are valid.
        if user_form.is_valid() and profile_form.is_valid():
            # Create a new user and save their information to the database.
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            # Create a UserProfile instance associated with the user.
            profile=profile_form.save(commit=False)
            profile.user= user

            # Check if a profile picture file was uploaded and assign it to the profile.
            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]

            # Save the profile to the database
            profile.save()

            # Set 'registered' to True to indicate a successful registration
            registerd=True

        else:
            # If forms are invalid, print validation errors for debugging
            print(user_form.errors,profile_form.errors)
    else:
        # For GET requests, create new instances of the forms to allow user input
        user_form=UserForm()
        profile_form=UserProfileForm()

    # Render the registration page with user and profile forms, and the 'registered' status
    return render(request,"Basic_App/registration.html",
                  {"user_form":user_form,
                   "profile_form":profile_form,
                   "registerd":registerd})

#User Login
def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user =authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        
        else:
            print("Some One Tried to Login and FAILED")
            print("Username: {} and Password {}".format(username,password))
            return HttpResponse ("Invalid Login details supplaied")

    else:
        return render(request,"Basic_App/login.html",{})
