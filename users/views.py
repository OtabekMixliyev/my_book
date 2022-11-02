from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreation


# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreation
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class Profile(CreateView):
    form_class = CustomUserCreation
    success_url = reverse_lazy('profile')
    template_name = 'profile.html'
