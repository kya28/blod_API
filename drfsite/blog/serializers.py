from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = "__all__"






