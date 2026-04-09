from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
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
        users.save()
        return super().form_valid(form)
class login(LoginView):
    template_name = "main/login.html"
    success_url = "/"
@method_decorator(login_required(login_url = 'login'),name='dispatch')
class home(TemplateView):
    template_name = "main/home.html"
class Cheack_balance(generic.DetailView):
    model = Userprofile
    template_name = "main/CheackBL.html"
    context_object_name = 'UserBlance'
    def get_object(self):
        return Userprofile.objects.get(user=self.request.user)
class Add_balance(generic.UpdateView):
    model = Userprofile
    fields =['balance']
    template_name = "main/addbalance.html"
    success_url = "/"
    def get_object(self):
        return Userprofile.objects.get(user = self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["balance"] = self.get_object().balance
        return context
    
    def post(self, request, *args, **kwargs):
        balance = int(self.request.POST['addbalance'])
        use = self.get_object()
        use.balance += balance
        use.save()
        return redirect('home')