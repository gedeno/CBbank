from django.urls import path
from .views import signup ,login ,home,Cheack_balance
from django.contrib.auth.views import LoginView,LogoutView 

urlpatterns = [
    path('signup/',signup.as_view(),name="signup"),
    path('login/',login.as_view(),name="login"),
    path('',home.as_view(),name="home"),
    path('Cheackbalance/',Cheack_balance.as_view(),name='Cheackbalance'),
    path('logout/',LogoutView.as_view(next_page = "login"), name = "logout"),

]

