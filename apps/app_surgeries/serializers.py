from rest_framework import serializers

from core.models.model_app_surgeries import Surgery


class SurgerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Surgery
        fields = ("id", "url", "name", )