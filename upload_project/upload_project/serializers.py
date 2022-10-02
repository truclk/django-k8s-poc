from rest_framework import serializers

from upload_project.models import PhotoModel
from upload_project.utils import confirm_upload


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = "__all__"

    def create(self, validated_data):
        if validated_data.get("internal_upload_link"):
            validated_data["internal_upload_link"], validated_data["upload_model_id"] = confirm_upload(
                validated_data.get("internal_upload_link")
            )
        return PhotoModel.objects.create(**validated_data)
