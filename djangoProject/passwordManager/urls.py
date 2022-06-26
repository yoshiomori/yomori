from django.urls import path

import passwordManager.views.password_create_view
import passwordManager.views.password_delete_view
import passwordManager.views.password_detail_view
import passwordManager.views.password_list_view
import passwordManager.views.password_update_view
from . import views

app_name = 'passwordManager'
urlpatterns = [
    path('list/', passwordManager.views.password_list_view.PasswordListView.as_view(), name='list'),
    path('detail/<int:pk>/', passwordManager.views.password_detail_view.PasswordDetailView.as_view(), name='detail'),
    path('create/', passwordManager.views.password_create_view.PasswordCreateView.as_view(), name='create'),
    path('update/<int:pk>/', passwordManager.views.password_update_view.PasswordUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', passwordManager.views.password_delete_view.PasswordDeleteView.as_view(), name='delete'),
]
