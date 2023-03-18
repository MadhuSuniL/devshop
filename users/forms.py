from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from .models import Developer


class DevCreationForm(UserCreationForm):
    class Meta:
        model = Developer
        fields = ("email",)
        
        

class DevChangeForm(UserChangeForm):
    class Meta:
        model = Developer
        fields = '__all__'

        