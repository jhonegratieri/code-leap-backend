from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

app_name = "posts"

post_api_router = SimpleRouter()
post_api_router.register(
    "careers",
    views.PostViewSet,
    basename="post-api",
)

urlpatterns = [
    path("", include(post_api_router.urls)),
]
