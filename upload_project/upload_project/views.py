from __future__ import absolute_import

import random
import time

from django.http.response import JsonResponse
from django.utils import timezone

import boto3
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from upload_project.models import PhotoModel
from upload_project.models import UploadModel
from upload_project.serializers import PhotoSerializer


class UploadSignS3ViewSet(APIView):
    # This would receive file-name and file-type to create a signed request to directly upload to S3.

    def get(self, request, *args, **kwargs):
        s3_upload_bucket = "truclk_testing_upload_bucket"
        max_file_size = 1048576
        try:
            boto_client = boto3.client("s3")
            time_prefix = str(int(time.mktime(timezone.now().timetuple())))
            project_folder = str("pulbic_upload")
            file_name = "%s/%s_%s_%s" % (
                project_folder,
                time_prefix,
                random.randint(1, 99),  # To reduce chance of duplication
                request.GET.get("file-name"),
            )
            file_type = request.GET.get("file-type")

            file_path = "https://%s.s3.amazonaws.com/%s" % (s3_upload_bucket, file_name)
            conditions = []
            conditions = [
                {"bucket": s3_upload_bucket},
                ["starts-with", "$key", file_name],
                {"acl": "public-read"},
            ]
            conditions += [
                {"Content-Type": file_type},
                ["content-length-range", 0, max_file_size],
            ]

            presigned_post = boto_client.generate_presigned_post(
                Bucket=s3_upload_bucket,
                Key=file_name,
                Fields={"Content-Type": file_type},
                Conditions=conditions,
                ExpiresIn=3600,
            )
            presigned_post["fields"]["acl"] = "public-read"
            client_upload_model, _ = UploadModel.objects.get_or_create(
                file_path=file_path
            )  # To reduce chance of duplication
            client_upload_model.file_name = file_name
            client_upload_model.status = UploadModel.STATUS_REQUESTED
            client_upload_model.save()
            return JsonResponse({"data": presigned_post, "url": file_path})
        except Exception as e:
            response = {"status": "error", "message": str(e)}
            return JsonResponse(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PhotoViewSet(ModelViewSet):
    queryset = PhotoModel.objects.all()
    serializer_class = PhotoSerializer
