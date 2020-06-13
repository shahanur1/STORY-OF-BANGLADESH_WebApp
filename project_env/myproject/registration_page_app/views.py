from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist!')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist!')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save()
                return redirect('/login_page')
            
        else:
            print('Password not matching.....')
            messages.info(request, 'Password not matching...')
            return redirect('register')

    else:
        return render(request, 'registration_page_app/registration_page.html')