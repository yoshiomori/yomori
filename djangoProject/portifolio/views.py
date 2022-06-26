from django.views import generic

from portifolio.models import App


class AppListView(generic.ListView):
    model = App
