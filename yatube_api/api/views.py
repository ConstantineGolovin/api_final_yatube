from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from posts.models import Group, Post, User

from .serializers import (CommentSerializer, GroupSerializer, PostSerializer,
                          UserSerializer, FollowSerializer)
from .permissions import IsAuthorOrReadOnlyPermission


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnlyPermission,
                          IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnlyPermission,
                          IsAuthenticatedOrReadOnly]

    def get_post(self):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, pk=post_id)

    def perform_create(self, serializer):
        serializer.save(post=self.get_post(), author=self.request.user)

    def get_queryset(self):
        return self.get_post().comments.all()


class FollowViewSet(ListModelMixin, CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'following__username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        return user.user_follower
