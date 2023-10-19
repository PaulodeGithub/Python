from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import UserRegistration, Login
from .forms import UserRegForm

def login_html_render(request):
    return render(request, "my_gym_app/login.html" )

def home_html_render(request):
    return render(request, "my_gym_app/home.html")


def home(request):
    return HttpResponse("Hello there, Your at the my_gym_app index.")

  
def verification(request):
    return render(request, "my_gym_app/verification.html")

def login_error(request):
    return render(request, "my_gym_app/login_error.html")
    
    
    
# def login(request):    
#     return HttpResponse("this is the login")
    

def registration(request):
    return render(request, "my_gym_app/register.html")
    

def reg_success(request):
    return render(request.method == 'POST', "my_gym_app/reg_success.html")




def login_verify_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print("email:", email)

        # must use username= email/ userrname, password are default settings
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Authentication was successful
            print("you logged in succesfully")
            login(request, user)
            messages.success(request, 'Successful login! ')
            return redirect('verification')  
        else:
            # Authentication failed
            print("you are not quite there yet, keep trying")
            messages.error(request, 'Invalid user!')
            return redirect('login_error')
        

    # # If it's not a POST request or authentication failed, render the login page
    # return render(request, 'my_gym_app/login.html')


# user registration form view

def reg_user_view(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            # Create a new UserRegistration instance and save it
            user = UserRegistration(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                date_of_birth=form.cleaned_data["date_of_birth"]
            )
            
            user.save()
            print("User registered, check the admin page to confirm")
            # Redirect to a success page or login page
            return redirect('reg_success')
    else:
        print("Somethings not quite right, take a breath, move with purpose")
        form = UserRegForm()

    return render(request, "my_gym_app/register.html", {"form": form})
    # return f"Somethings not quite right, take a breath, move with purpose"  