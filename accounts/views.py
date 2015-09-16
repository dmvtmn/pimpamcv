from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate

from .forms import LoginForm,RegistrationForm
# Create your views here.

def logout_view(request):
    logout(request)#logsout of the request
    return HttpResponseRedirect('/') #upon logout go to home page


def login_view(request):

    form = LoginForm(request.POST or None)#take in the POST request data, or nothing and just render
    btn = 'Entrar'
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)# checking credentials of the user
        login(request,user)
        user.emailconfirmed.active_user_email()

    context = {
    "form": form,
    "submit_btn" : btn,
    }
    return render(request, "form.html", context)

def registration_view(request):

    form = RegistrationForm(request.POST or None)#take in the POST request data, or nothing and just render
    btn = 'Registrate'

    if form.is_valid():
        new_user = form.save(commit=False)
        #new_user.first_name = "Daniel"
        new_user.save()


        '''
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)# checking credentials of the user
        login(request,user)
        '''

    context = {
    "form": form,
    "submit_btn" : btn,
    }
    return render(request, "form.html", context)
