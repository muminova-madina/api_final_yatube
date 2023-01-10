from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Group, Post, Comment, Follow

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(read_only=True,
                                              source='post.pk')
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username',
                                          required=False)

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    class Meta:
        fields = '__all__'
        model = Follow

    def validate(self, data):
        author = data['following']
        user = self.context['request'].user
        if author == user:
            raise serializers.ValidationError('Подписка на самого себя!')
        if author.following.filter(user_id=user.id).exists():
            raise serializers.ValidationError('Подписка существует!')

        return data


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('__all__')
