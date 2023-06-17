from django.urls import path
from products.views import HashtagModelViewSet, HashtagCategoryAPIView, HashtagAPIView

app_name = "hashtags"

urlpatterns = [
    path("", HashtagModelViewSet.as_view({'get': 'list', 'post': 'create'}), name="list-create"),
    path("categories/", HashtagCategoryAPIView.as_view(), name="cate-list"),
    path("detail/<int:id>/", HashtagAPIView.as_view(), name="detaul-get"),
]
