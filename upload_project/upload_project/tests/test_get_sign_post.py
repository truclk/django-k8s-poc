from __future__ import absolute_import

import json
from unittest.mock import patch

from upload_project.models import UploadModel


def test_get_signed_url(client, transactional_db):
    with patch("upload_project.views.time") as mock_time:
        with patch("upload_project.views.boto3") as mock_get_client:
            with patch("upload_project.views.random") as mock_random:
                mock_get_client.client.return_value.generate_presigned_post.return_value = {
                    "url": "https://truclk_testing_upload_bucket.s3.amazonaws.com/pulbic_upload/1521524302_1_abc.txt",
                    "fields": {},
                }
                mock_random.randint.return_value = 1
                mock_time.mktime.return_value = 1521524302.0

                response = client.get("/upload/sign_s3", {"file-name": "abc.txt", "file-type": "image"})
                data = json.loads(response.content)
                assert (
                    data["url"].startswith(
                        "https://truclk_testing_upload_bucket.s3.amazonaws.com/pulbic_upload/1521524302_1_abc.txt"
                    )
                    == True
                )
                upload_model = UploadModel.objects.filter(file_name="pulbic_upload/1521524302_1_abc.txt").first()
                assert UploadModel.STATUS_REQUESTED == upload_model.status
