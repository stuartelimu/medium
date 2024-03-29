from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    get_object_or_404, 
    GenericAPIView, 
    RetrieveUpdateDestroyAPIView, 
    ListAPIView, ListCreateAPIView
    )
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from .models import Article, Author
from .serializers import ArticleSerializer


class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)


class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    