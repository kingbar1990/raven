from rest_framework import serializers

from core.models.model_app_users import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    info = serializers.JSONField()
    class Meta:
        model = User
        fields = ("id", "url", "full_name", "email", "info")