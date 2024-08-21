from django.urls import path

from service.apps import ServiceConfig
from service.views import (
    ServiceHomeView,
    ServiceListView,
    ServiceCreateView,
    ServiceDetailView,
    ServiceUpdateView,
    ServiceDeleteView,
    SignUpCreateView,
    sign_up,
    sign_up_info,
    SignUpUpdateView,
    SignUpListView,
    SignUpDeleteView,
)

app_name = ServiceConfig.name

urlpatterns = [
    path("", ServiceHomeView.as_view(), name="home"),
    path("services/", ServiceListView.as_view(), name="list-service"),
    path("create/", ServiceCreateView.as_view(), name="create-service"),
    path("detail/<int:pk>/", ServiceDetailView.as_view(), name="detail-service"),
    path("update/<int:pk>/", ServiceUpdateView.as_view(), name="update-service"),
    path("delete/<int:pk>/", ServiceDeleteView.as_view(), name="delete-service"),
    path("signup/create/", SignUpCreateView.as_view(), name="create-signup"),
    path("signup/<int:pk>/", sign_up, name="sign_up"),
    path("signup/info/<int:pk>/", sign_up_info, name="sign_up_info"),
    path("signup/update/<int:pk>/", SignUpUpdateView.as_view(), name="update-signup"),
    path("signup/", SignUpListView.as_view(), name="list-signup"),
    path("signup/delete/<int:pk>/", SignUpDeleteView.as_view(), name="delete-signup"),
]
