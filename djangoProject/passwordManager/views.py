from django.urls import reverse_lazy
from django.views import generic

from passwordManager.models import Password


class PasswordListView(generic.ListView):
    model = Password


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
