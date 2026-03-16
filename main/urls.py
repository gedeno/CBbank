from django.urls import path
from .views import signup ,login 

urlpatterns = [
    path('signup/',signup.as_view(),name="signup"),
    path('login/',login.as_view(),name="login"),
    
]

