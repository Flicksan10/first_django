# w pliku forms.py twojej aplikacji
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Message

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


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'topic', 'content']
class ReplyMessageForm(MessageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('receiver')  # Usunięcie pola receiver
