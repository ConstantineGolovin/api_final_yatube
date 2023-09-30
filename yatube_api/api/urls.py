from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

app_name = 'api'

router_v1 = SimpleRouter()
router_v1.register(r'posts', PostViewSet)
router_v1.register(r'groups', GroupViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comment')
router_v1.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
