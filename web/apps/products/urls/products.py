from django.urls import path
from products.views import ProductModelViewSet
from products.views import ProductHashtagCreateAPIView

app_name = "products"

urlpatterns = [
    path("", ProductModelViewSet.as_view({'get': 'list', 'post': 'create'}), name="list-create"),
    # path("", ProductModelViewSet.as_view(), name="list-create"),
    path("hashtags/", ProductHashtagCreateAPIView.as_view(), name="connect_hashtag"),
]
