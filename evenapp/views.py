from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from evenapp.forms import registrationForm, ReviewForm
from evenapp.models import photo, Review, Contact
from django.shortcuts import render, redirect
from django.contrib.auth.models import User



# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    logout(request)
    return render(request,'about.html')




def gallery(request):
    photos = photo.objects.all()

    return render(request,'gallery.html',{'photos': photos})


def service(request):
    return render(request,'services.html')

def booking(request):
    s3=registrationForm()
    form = {'register': s3}
    if request.method == 'POST':
        s3=registrationForm(request.POST)
        if s3.is_valid():
            s3.save()
    return render(request, 'booking.html', form)


def review_page(request):
    if request.method == 'POST':
        form1 = ReviewForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('suggestions')
    else:
        form1 = ReviewForm()

    reviews = Review.objects.all()
    return render(request, 'suggestion.html', {'form': form1, 'reviews': reviews})


def contact_page(request):
    s1=Contact.objects.all()
    d1={'key':s1}
    return render(request,'contact.html',d1)






def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'signup.html', {'error_message': 'Passwords do not match'})

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error_message': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error_message': 'Email already exists'})

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password,
                                        first_name=first_name, last_name=last_name)

        # Redirect to a success page or login page
        return redirect('login')
    else:
        return render(request, 'signup.html')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def logout(request):
    return redirect('login')
def send_email(request):
    send_mail(
        'Checking Mail in Django',
        'Message shared using Email programmed using Django',
        'bijinkichu1993@gmail.com',
        ['jishabijin1997@gmail.com'],
        fail_silently=False)

    return render(request, 'contact.html')



