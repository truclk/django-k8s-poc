from rest_framework import serializers

from upload_project.models import PhotoModel


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = "__all__"
