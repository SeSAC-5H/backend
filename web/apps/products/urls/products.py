from django.urls import path
from products.views import ProductListCreateAPIView
from products.views import ProductHashtagCreateAPIView

app_name = "products"

urlpatterns = [
    path("", ProductListCreateAPIView.as_view(), name="create"),
    path("hashtags/", ProductHashtagCreateAPIView.as_view(), name="connect_hashtag"),
]
