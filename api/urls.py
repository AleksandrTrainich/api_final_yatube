from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='Posts')
router.register('group', GroupViewSet, basename='Groups')
router.register('follow', FollowViewSet, basename='Follows')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='Comments')
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
