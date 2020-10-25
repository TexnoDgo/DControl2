from rest_framework import serializers
from .models import TestModel


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestModel
        fields = "__all__"

