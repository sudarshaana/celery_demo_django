from django.urls import path

app_name = "celery_test"

from . import views

urlpatterns = [
    path("celery_task", views.test, name="test"),
]
