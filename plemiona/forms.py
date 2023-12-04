# w pliku forms.py twojej aplikacji
from django import forms
from django.contrib.auth.forms import AuthenticationForm

# Nie musisz niczego dodawać do tej klasy, jeśli używasz standardowego formularza Django,
# ale możesz ją rozszerzyć, jeśli potrzebujesz niestandardowej logiki.
# class UserLoginForm(AuthenticationForm):
#     pass


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomLoginForm(AuthenticationForm):
    # Dodaj swoje dodatkowe pola
    pass
    # custom_field = forms.CharField(required=False)


class MessageForm(forms.Form):
    receiver = forms.CharField(max_length=100)
    topic = forms.CharField(max_length=100, label='Temat')
    content = forms.CharField(widget=forms.Textarea)
    # to let answer to message
    reply_to = forms.IntegerField(required=False, widget=forms.HiddenInput())