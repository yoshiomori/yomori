from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from passwordManager.models import Password
from passwordManager.views.commons.password_field_view_mixin import PasswordFieldViewMixin


class PasswordCreateView(LoginRequiredMixin, PasswordFieldViewMixin, generic.CreateView):
    model = Password
    fields = ['password', 'username', 'description', 'title']
    title = 'New Password'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
