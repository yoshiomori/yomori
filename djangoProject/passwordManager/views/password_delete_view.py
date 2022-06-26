from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from passwordManager.models import Password


class PasswordDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Password
    success_url = reverse_lazy('passwordManager:list')
    title = 'Delete Password'
