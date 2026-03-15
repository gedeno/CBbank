from django.shortcuts import render
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
    template_name = "signup.html"
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

        
        
