from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

from . import views

app_name = "posts"

schema_view = get_schema_view(
    openapi.Info(
        title="CRUD POSTS API",
        default_version="v1",
        description="Create, Read, Update and Delete (CRUD) Posts",
        contact=openapi.Contact(email="jhonatansimoni@gmail.com"),
        license=openapi.License(name="Jhonatan Gratieri Simoni"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


post_api_router = SimpleRouter()
post_api_router.register(
    "careers",
    views.PostViewSet,
    basename="post-api",
)

urlpatterns = [
    path("", include(post_api_router.urls)),
]

urlpatterns += [
    path(
        "swagger<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
