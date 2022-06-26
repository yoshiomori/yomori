from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from passwordManager.models import Password


class PasswordDetailView(LoginRequiredMixin, generic.DetailView):
    model = Password
    title = 'Password'
