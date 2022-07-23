from django.urls import path

from .views import StudentLC

urlpatterns = [
    path("all_students", StudentLC.as_view(), name="get_all_students"),
]
