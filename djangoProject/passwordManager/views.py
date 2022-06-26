from django.urls import reverse_lazy
from django.views import generic

from passwordManager.filters.passwordFilter import PasswordFilter
from passwordManager.models import Password


class PasswordListView(generic.ListView):
    model = Password

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
        return self.password_filter.filter_queryset(super().get_queryset())


class PasswordDetailView(generic.DetailView):
    model = Password


class PasswordCreateView(generic.CreateView):
    model = Password
    fields = '__all__'


class PasswordUpdateView(generic.UpdateView):
    model = Password
    fields = '__all__'


class PasswordDeleteView(generic.DeleteView):
    model = Password
    success_url = reverse_lazy('passwordManager:list')
