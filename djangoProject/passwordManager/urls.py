from django.urls import path

from . import views

app_name = 'passwordManager'
urlpatterns = [
    path('list/', views.PasswordListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.PasswordDetailView.as_view(), name='detail'),
    path('create/', views.PasswordCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.PasswordUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PasswordDeleteView.as_view(), name='delete'),
]
