from rest_framework import serializers
from userinfo.serializers import UserDescSerializer
from info.models import Infos


class InfoListSerializer(serializers.ModelSerializer):
    """
    Infos list serializer
    """
    author = UserDescSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='info:detail', lookup_field='pk')

    class Meta:
        model = Infos
        fields = [
            # 'id',
            'title',
            'time',
            'author',
            'url'
        ]


class InfoDetailSerializer(serializers.ModelSerializer):
    """
    Infos detial serializer
    """

    class Meta:
        model = Infos
        fields = '__all__'
