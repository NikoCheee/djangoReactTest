from rest_framework import  serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    owner = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ('pk', 'title', 'content', 'author', 'owner', 'tags')
