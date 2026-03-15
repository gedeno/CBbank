from django.shortcuts import render
from django.contrib.auth.forms import UserCrationform 
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import TemplateView
from django.views import generic
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User

# Create your views here.