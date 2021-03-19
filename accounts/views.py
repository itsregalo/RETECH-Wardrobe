from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import  send_mail
from django.template.loader import render_to_string

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_gen

from django.contrib.auth import get_user_model
User = get_user_model()

import threading
# Create your views here.

class EmailThread(threading.Thread):
    def __init__(self, mail):
        self.mail = mail
        threading.Thread.__init__(self)
        
    def run(self):
        self.mail.send_mail()

def LogInView(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        if username == "":
            messages.error(request, "Username required")
        if password == "":
            messages.error(request, "Password is required")
        
        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            login(request, user)
            messages.info(request, "You have successfully logged in")
            return redirect('retechecommerce:index')
        else:
            messages.error(request,"Ivalid Login")
            return render(request,'auth/login.html')
    return render(request, 'auth/login.html', {})

def LogOutView(request, *args, **kwargs):
    logout(request)
    messages.success(request,"You have successfully Logged Out")
    return redirect('retechecommerce:index')

def RegisterView(request):
    
    if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            
            
            if username == "":
                messages.error(request, "Username is required")
            if email == "":
                messages.error(request, "Email is required")
            if password1 == "":
                messages.error(request, "Password is required")
            if password2 == "":
                messages.error(request, "Repeat Password is required")
                return redirect('accounts:register')
            
            if User.objects.filter(username=username).exists():
                messages.error(request, "A user with the username exists")
            if User.objects.filter(email=email).exists():
                messages.error(request, "The Email has already been taken")
                return redirect('accounts:register') 
            
            if password1 != password2:
                messages.error(request, "Passwords do not match")
            if len(password1)<6:
                messages.error(request,"Password is too short")
                return redirect('accounts:register') 
              
                    

                    
            else:
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password1)
                user.is_active=False
                user.save()
                
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                domain = get_current_site(request).domain #gives us the domain
                link = reverse('accounts:activate', 
                                kwargs={
                                    'uidb64':uidb64, 
                                    'token':token_gen.make_token(user)
                                        })
                activate_url = f"http://{domain+link}"
                
                mail_subject = "Activate your account"
                
                """
                message = render_to_string('auth/activate.html', {
                    'user':user,
                    'domain':domain,
                    'uidb64':uidb64,
                    'token':token_gen.make_token(user)
                })
                """
                
                mail_body = f"hi {user.username} click the link below to verify your account\n {activate_url}"
                mail = send_mail (mail_subject, mail_body,'noreply@retech.com',[email], fail_silently=False)
                messages.success(request, "User has been created")
                return redirect('accounts:login')
            
    return render(request, 'auth/register.html', {})

def VerificationView(request,uidb64, token):

    uidb = force_text(urlsafe_base64_decode(uidb64)) or None
    user = User.objects.get(pk=uidb) or None

        
    if user is not  None and token_gen.check_token(user, token):
        user.is_active=True
        user.save()
        messages.info(request, "account verified")  
        return redirect("accounts:login")
    return render(request,'auth/activation_failed.html')

def SetNewPassword(request, uidb64, token):
    user_id = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=user_id)
    