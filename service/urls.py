from django.urls import path

from service.apps import ServiceConfig
from service.views import (
    ServiceListView,
    ServiceCreateView,
    ServiceDetailView,
    ServiceUpdateView,
    ServiceDeleteView,
)

app_name = ServiceConfig.name

urlpatterns = [
    path("", ServiceListView.as_view(), name="home"),
    path("create/", ServiceCreateView.as_view(), name="create-service"),
    path("detail/<int:pk>/", ServiceDetailView.as_view(), name="detail-service"),
    path("update/<int:pk>/", ServiceUpdateView.as_view(), name="update-service"),
    path("delete/<int:pk>/", ServiceDeleteView.as_view(), name="delete-service"),
]
