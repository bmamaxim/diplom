from django.urls import path

from employee.apps import EmployeeConfig
from employee.views import (
    EmployeeListView,
    EmployeeCreateView,
    EmployeeDetailView,
    EmployeeUpdateView,
    EmployeeDeleteView,
)

app_name = EmployeeConfig.name

urlpatterns = [
    path("", EmployeeListView.as_view(), name="employee"),
    path("create/", EmployeeCreateView.as_view(), name="create-employee"),
    path("detail/<int:pk>/", EmployeeDetailView.as_view(), name="detail-employee"),
    path("update/<int:pk>/", EmployeeUpdateView.as_view(), name="update-employee"),
    path("delete/<int:pk>/", EmployeeDeleteView.as_view(), name="delete-employee"),
]
