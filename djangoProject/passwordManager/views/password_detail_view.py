from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import generic

from passwordManager.models import Password


class PasswordDetailView(LoginRequiredMixin, generic.DetailView):
    model = Password
    title = 'Password'

    def get_queryset(self):
        return super().get_queryset().filter(Q(user=self.request.user))
