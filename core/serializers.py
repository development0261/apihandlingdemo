from rest_framework import serializers

from .models import APIDATA


class APIDATASerializer(serializers.ModelSerializer):
    class Meta:
        model = APIDATA
        fields = "__all__"
