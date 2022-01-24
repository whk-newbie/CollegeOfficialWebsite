from news.models import News
from news.serializers import NewsListSerializer, NewsDetailSerializer
from rest_framework import generics
from news.permissions import IsAdminUserOrReadOnly


class NewsList(generics.ListCreateAPIView):
    # 权限设置
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = News.objects.all()
    serializer_class = NewsListSerializer


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Create your views here.
# class AvatarViewSet(viewsets.ModelViewSet):
#     queryset = Avatar.objects.all()
#     serializer_class = AvatarSerializer
