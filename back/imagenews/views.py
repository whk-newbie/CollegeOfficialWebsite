from imagenews.models import ImageNews
from imagenews.serializers import ImageNewsListSerializer, ImageNewsDetailSerializer
from rest_framework import generics
from news.permissions import IsAdminUserOrReadOnly


class ImageNewsList(generics.ListCreateAPIView):
    # 权限设置
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = ImageNews.objects.all()
    serializer_class = ImageNewsListSerializer


class ImageNewsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = ImageNews.objects.all()
    serializer_class = ImageNewsDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Create your views here.
# class AvatarViewSet(viewsets.ModelViewSet):
#     queryset = Avatar.objects.all()
#     serializer_class = AvatarSerializer
