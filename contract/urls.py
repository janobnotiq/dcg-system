from django.urls import path
from .views import company_report


urlpatterns = [
    path("company-report/<int:pk>/", company_report, name="company-report"),
]