from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from passwordManager.models import Password


class PasswordCreateView(LoginRequiredMixin, generic.CreateView):
    model = Password
    fields = ['password', 'username', 'description', 'title']
    title = 'New Password'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
