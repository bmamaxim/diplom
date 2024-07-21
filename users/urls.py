from django.urls import path

from users.apps import UsersConfig
from users.views import (
    UsersListView,
    UsersCreateView,
    UsersDetailView,
    UsersUpdateView,
    UsersDeleteView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("", UsersListView.as_view(), name="users"),
    path("create/", UsersCreateView.as_view(), name="create-user"),
    path("detail/<int:pk>/", UsersDetailView.as_view(), name="detail-user"),
    path("update/<int:pk>/", UsersUpdateView.as_view(), name="update-user"),
    path("delete/<int:pk>/", UsersDeleteView.as_view(), name="delete-user"),
]
