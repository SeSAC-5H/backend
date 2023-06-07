from django.urls import path
from products.views import ProductCreateAPIView
from products.views import ProductHashtagCreateAPIView

app_name = "products"

urlpatterns = [
    path("", ProductCreateAPIView.as_view(), name="create"),
    path("hashtags/", ProductHashtagCreateAPIView.as_view(), name="connect_hashtag"),
]
