from django.urls import path
from stores.views import StoreListCreateAPIView, ReportCreateAPIView


app_name = "stores"

urlpatterns = [
    path("", StoreListCreateAPIView.as_view(), name="list-create"),
    path("report/", ReportCreateAPIView.as_view(), name="report-create"),
]
