# w pliku forms.py twojej aplikacji
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Message
from .models import MessageThread
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


from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label='content_label')

    class Meta:
        model = Message
        fields = ['receiver', 'subject']




from django import forms
from .models import MessageThread

class MessageThreadForm(forms.ModelForm):
    class Meta:
        model = MessageThread
        fields = ['content']


        # 'content' to pole w modelu MessageThread, które przechowuje treść odpowiedzi
