from typing import Any
from django.shortcuts import render,redirect
from . import forms
from carmodel.forms import CarForm
from django.contrib import messages
from django.contrib.auth.views import LoginView 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from carmodel.models import CarModel
from django.views.generic import ListView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
# Create your views here.

class UserLogin(LoginView):
    template_name = 'register.html'
    def form_valid(self, form):
        messages.success(self.request,"Logged in successfully")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request," Logged information incorrect ")
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('profile')
    

def register(request):
    if request.method == 'POST':
        form =forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form =forms.RegistrationForm()
    return render(request,'register.html',{'form':form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@method_decorator(login_required,name=('dispatch'))
class ProfileView(ListView):
    template_name = 'profile.html'
    context_object_name = 'data'
    def get_queryset(self):
        return CarModel.objects.filter(author=self.request.user)




@login_required
def buy_now(request, id):
    car_model = get_object_or_404(CarModel, pk=id)
    car_model.author = request.user

    if car_model.quantity > 0:
        
        car_model.quantity -= 1
        car_model.save()

        messages.success(request, f"You've successfully purchased {car_model.car_name}")
    else:
        messages.warning(request, f"Sorry, {car_model.car_name} is out of stock.")

    return redirect('profile')


@login_required
def pass_change(request):
    if request.method == 'POST':
        form =PasswordChangeForm(user =request.user , data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'pass.html' ,{'form':form})
            
        