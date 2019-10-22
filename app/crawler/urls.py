from django.conf.urls import url, include
from rest_framework import routers
from api.views.user_view import UserViewSet
from api.views.feed_view import FeedViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    
    url(r'^', include(router.urls)),

    url(r'^feed/', FeedViewSet.as_view({'get':'list'})),

    url(r'^api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]