from django.forms import ModelForm
from .models import Userprofile

class UserprofileForm(ModelForm):
    class Meta:
        model = Userprofile
        fields = "__all__"
        exclude = ['user']
        