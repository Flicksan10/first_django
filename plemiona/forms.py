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


from django import forms
from .models import Topic_message

class MessageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label='content_label')

    class Meta:
        model = Topic_message
        fields = ['receiver', 'subject']




from django import forms
from .models import Answers_Message

class MessageThreadForm(forms.ModelForm):
    class Meta:
        model = Answers_Message
        fields = ['content']


        # 'content' to pole w modelu MessageThread, które przechowuje treść odpowiedzi
