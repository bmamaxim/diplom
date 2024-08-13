from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (
    UsersListView,
    UsersCreateView,
    UsersDetailView,
    UsersUpdateView,
    UsersProfileView,
    UsersDeleteView,
    Verify,
)

app_name = UsersConfig.name

urlpatterns = [
    path("", UsersListView.as_view(), name="users"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("verify/", Verify.as_view(), name="verify"),
    path("create/", UsersCreateView.as_view(), name="create-user"),
    path("detail/<int:pk>/", UsersDetailView.as_view(), name="detail-user"),
    path("profile/", UsersProfileView.as_view(), name="profile"),
    path("update/<int:pk>/", UsersUpdateView.as_view(), name="update-user"),
    path("delete/<int:pk>/", UsersDeleteView.as_view(), name="delete-user"),
]
