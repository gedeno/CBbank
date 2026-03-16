from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from .models import Userprofile
from .forms import UserprofileForm

# Create your views here.
class signup(FormView):
    template_name = "main/signup.html"
    form_class = UserCreationForm 
    success_url = "/login/"
    def form_valid(self, form):
        acc_no = 100050700 + User.objects.count()
        username = form.cleaned_data.get("username")
        user = form.save()
        users = Userprofile.objects.create(
            Username = username,
            acc_no = acc_no,
            user = user
        )
        user.save()
        return super().form_valid(form)
class login(LoginView):
    template_name = "main/login.html"
    success_url = "/"
class home(LoginRequiredMixin):
    template_name = "main/home.html"
class Cheack_balance(generic.ListView):
    template_name = "main/CheackBL.html"
    context_object_name = 'UserBlance'
    def get_queryset(self):
        return Userprofile.objects.filter(user=self.request.user)
    
