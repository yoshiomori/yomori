import django_filters
from django.db.models import Q

from passwordManager.models import Password


class PasswordFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='password_filter', label="Search")

    class Meta:
        model = Password
        fields = ['q']

    @staticmethod
    def password_filter(queryset, name, value):
        return queryset.filter(Q(title__icontains=value) | Q(description__icontains=value))
