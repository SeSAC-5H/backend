from django.urls import path
from products.views import BrandCreateAPIView

app_name = "brands"

urlpatterns = [
    path("", BrandCreateAPIView.as_view(), name="create"),
]
