from django.urls import path
from products.views import HashtagListCreateAPIView

app_name = "hashtags"

urlpatterns = [
    path("", HashtagListCreateAPIView.as_view(), name="list-create"),
]
