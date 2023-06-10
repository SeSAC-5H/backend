from django.urls import path
from stores.views import StoreListCreateAPIView


app_name = "stores"

urlpatterns = [
    path("", StoreListCreateAPIView.as_view(), name="list-create"),
]
