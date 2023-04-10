from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()

router.register("profiles_set", views.HelloViewSet, basename="profile")
router.register("profile", views.UserProfileViewSet)

urlpatterns = [
    path("profiles_view/", views.HelloApiView.as_view()),
    path("", include(router.urls)),
]
