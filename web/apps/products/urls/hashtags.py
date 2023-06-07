from django.urls import path
from products.views import HashtagCreateAPIView

app_name = "hashtags"

urlpatterns = [
    path("", HashtagCreateAPIView.as_view(), name="create"),
]
