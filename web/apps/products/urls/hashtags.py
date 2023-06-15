from django.urls import path
from products.views import HashtagListCreateAPIView, HashtagCategoryAPIView, HashtagAPIView

app_name = "hashtags"

urlpatterns = [
    path("", HashtagListCreateAPIView.as_view(), name="list-create"),
    path("categories/", HashtagCategoryAPIView.as_view(), name="cate-list"),
    path("detail/<int:id>/", HashtagAPIView.as_view(), name="detaul-get"),
]
