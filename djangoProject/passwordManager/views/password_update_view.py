from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from passwordManager.models import Password


class PasswordUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Password
    fields = '__all__'
    title = 'Update Password'
