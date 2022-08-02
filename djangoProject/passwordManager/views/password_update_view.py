from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from passwordManager.models import Password
from passwordManager.views.commons.password_field_view_mixin import PasswordFieldViewMixin


class PasswordUpdateView(LoginRequiredMixin, PasswordFieldViewMixin, generic.UpdateView):
    model = Password
    fields = ['password', 'username', 'description', 'title']
    title = 'Update Password'
