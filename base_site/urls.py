from django.urls import include, path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("sb/wake-up", views.wake_up),
]
