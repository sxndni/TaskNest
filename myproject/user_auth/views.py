from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def user_login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        u=authenticate(username=username,password=password)
        if u:
            login(request,u)
            
            return redirect('home')
        else:
            return render(request,'login.html',{'status':True})
    return render(request,'login.html')

def register(request):
    
    
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confirm = request.POST['confirm_password']

        
        # if password != confirm:
        #     return render(request, 'register.html', {
        #         'status': True,
        #         'error': 'Passwords do not match'
        #     })

        
        # if len(password) < 8 or len(password) > 16:
        #     return render(request, 'register.html', {
        #         'status': True,
        #         'error': 'Password must be 8–16 characters long'
        #     })

        # has_upper = any(ch.isupper() for ch in password)
        # has_lower = any(ch.islower() for ch in password)
        # has_digit = any(ch.isdigit() for ch in password)
        # special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>?/|\\"
        # has_special = any(ch in special_chars for ch in password)

        # if not has_upper:
        #     return render(request, 'register.html', {
        #         'status': True,
        #         'error': 'Password must contain an uppercase letter'
        #     })
        # if not has_lower:
        #     return render(request, 'register.html', {
        #         'status': True,
        #         'error': 'Password must contain a lowercase letter'
        #     })
        # if not has_digit:
        #     return render(request, 'register.html', {
        #         'status': True,
        #         'error': 'Password must contain a number'
        #     })
        # if not has_special:
        #     return render(request, 'register.html', {
        #         'status': True,
        #         'error': 'Password must contain a special character'
        #     })
        print(fname,lname,email,username,password)
        try:
            u=User.objects.get(username=username)
            return render(request,'register.html',{'status':True})
        except:
            u=User.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            username=username,
            
            )
            u.set_password(password)
            u.save()

            return redirect('login')
        
    
    return render(request,'register.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def profile(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        u=request.user
        u.username=username
        u.email=email
        u.save()
        return redirect('profile')
    return render(request,'profile.html')

def reset_password(request):
    u=User.objects.get(username=request.user)
    if request.method=='POST':
        try:
            old_pass=request.POST['oldpass']
            verified=authenticate(username=u.username,password=old_pass)
            if verified:
                return render(request,'reset_password.html',{'verified':True})
            else:
                return render(request,'reset_password.html',{'not_verified':True})
        except: 
            new_pass=request.POST['newpass']
            u.set_password(new_pass)
            u.save()
            return redirect('login')

    return render(request,'reset_password.html')