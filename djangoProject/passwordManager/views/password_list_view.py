from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import generic

from passwordManager.filters.passwordFilter import PasswordFilter
from passwordManager.models import Password


class PasswordListView(LoginRequiredMixin, generic.ListView):
    model = Password
    title = 'Password Manager'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password_filter = None
        self.password_filter: PasswordFilter

    def dispatch(self, request, *args, **kwargs):
        self.password_filter = PasswordFilter(request.GET, request=request)
        self.password_filter.is_valid()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(filter=self.password_filter, **kwargs)

    def get_queryset(self):
        return self.password_filter.filter_queryset(super().get_queryset().filter(Q(user=self.request.user)))
