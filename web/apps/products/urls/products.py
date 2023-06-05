from django.urls import path
from products.views import ProductCreateAPIView

app_name = "products"

urlpatterns = [
    path("", ProductCreateAPIView.as_view(), name="create"),
]
