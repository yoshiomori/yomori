from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from passwordManager.models import Password


class PasswordCreateView(LoginRequiredMixin, generic.CreateView):
    model = Password
    fields = '__all__'
    title = 'New Password'
