from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet, FollowViewSet, GroupViewSet

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')
v1_router.register('groups', GroupViewSet, basename='group')
v1_router.register('follow', FollowViewSet, basename='follow')

jwt_patterns = [path('', include('djoser.urls')),
                path('', include('djoser.urls.jwt'))
]

urlpatterns = [
    path('v1/', include(jwt_patterns)),
    path('v1/', include(v1_router.urls))
]
