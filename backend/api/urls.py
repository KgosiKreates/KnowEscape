from django.urls import path

from .views import LeisaExportView

urlpatterns = [
    path("exports/leisa/", LeisaExportView.as_view(), name="leisa-export"),
]