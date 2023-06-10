from django.urls import path
from products.views import HashtagListCreateAPIView, HashtagCategoryAPIView

app_name = "hashtags"

urlpatterns = [
    path("", HashtagListCreateAPIView.as_view(), name="list-create"),
    path("categories/", HashtagCategoryAPIView.as_view(), name="cate-list"),
]
