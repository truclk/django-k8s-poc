from __future__ import absolute_import

import pytest

from upload_project.models import PhotoModel
from upload_project.models import UploadModel


@pytest.fixture()
def uploaded_file(transactional_db):
    upload_model = UploadModel.objects.create(
        status=UploadModel.STATUS_REQUESTED, file_name="123_abc.text", file_path="upload_path/123_abc.txt"
    )
    return upload_model


def test_create_photo(client, transactional_db, uploaded_file):
    response = client.post("/photo/", {"internal_upload_link": "upload_path/123_abc.txt"})
    photo = PhotoModel.objects.first()
    assert photo.internal_upload_link
    assert photo.upload_model
    assert response.status_code == 201
