# w pliku forms.py twojej aplikacji

from django.contrib.auth.forms import AuthenticationForm

# Nie musisz niczego dodawać do tej klasy, jeśli używasz standardowego formularza Django,
# ale możesz ją rozszerzyć, jeśli potrzebujesz niestandardowej logiki.
class UserLoginForm(AuthenticationForm):
    pass
