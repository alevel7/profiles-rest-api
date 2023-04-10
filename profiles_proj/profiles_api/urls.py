from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()

router.register("profiles_set", views.HelloViewSet, basename="profile")
router.register("profile", views.UserProfileViewSet)
router.register("feed", views.UserProfileFeedViewSet)

urlpatterns = [
    path("profiles_view/", views.HelloApiView.as_view()),
    path("login/", views.UserLoginApiView.as_view()),
    path("", include(router.urls)),
]
