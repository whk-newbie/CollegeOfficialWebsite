from info.models import Infos
from rest_framework import generics
from info.serializers import InfoListSerializer, InfoDetailSerializer
from news.permissions import IsAdminUserOrReadOnly


# Create your views here.
class InfoList(generics.ListCreateAPIView):
    # 权限设置
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Infos.objects.all()
    serializer_class = InfoListSerializer


class InfoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Infos.objects.all()
    serializer_class = InfoDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
