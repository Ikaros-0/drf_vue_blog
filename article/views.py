from article.models import Article, Category, Tag, Avatar
from article.serializers import ArticleSerializer, CategorySerializer, CategoryDetailSerializer, TagSerializer, ArticleDetailSerializer, AvatarSerializer
from django.shortcuts import render
from rest_framework import status, viewsets, filters
from article.permissions import IsAdminUserOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

# # Create your views here.

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend,]
    # search_fields = ['title', 'author__username']
    filterset_fields = ['author__username', 'title']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    # serializer_class = CategoryDetailSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryDetailSerializer
        
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    