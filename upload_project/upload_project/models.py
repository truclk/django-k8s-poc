from __future__ import absolute_import

from django.db import models

from model_utils.models import TimeStampedModel


class PhotoModel(TimeStampedModel):
    UPLOAD_TYPE_EQUIPMENT = "equipment"
    UPLOAD_TYPE_SUMMIT = "summit"
    UPLOAD_TYPE_CHOICES = (
        (UPLOAD_TYPE_EQUIPMENT, "Equipment"),
        (UPLOAD_TYPE_SUMMIT, "Summit photo"),
    )
    upload_type = models.CharField(max_length=25, default=UPLOAD_TYPE_EQUIPMENT, choices=UPLOAD_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    surname = models.CharField(max_length=1024, blank=True, null=True)
    firstname = models.CharField(max_length=1024, blank=True, null=True)
    birthyear = models.CharField(max_length=1024, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    postcode = models.CharField(max_length=1024, blank=True, null=True)
    town = models.CharField(max_length=1024, blank=True, null=True)
    telephone = models.CharField(max_length=1024, blank=True, null=True)
    email = models.CharField(max_length=1024, blank=True, null=True)
    DONATE_TYPE_SWISS_MUSEUM = "museum"
    DONATE_TYPE_LAF_2023 = "laf_2023"
    DONATE_TYPE_CHOICES = (
        (DONATE_TYPE_SWISS_MUSEUM, "Swiss Museum"),
        (
            DONATE_TYPE_LAF_2023,
            "LAF 202",
        ),
    )
    donate_type = models.CharField(max_length=25, default=DONATE_TYPE_SWISS_MUSEUM, choices=DONATE_TYPE_CHOICES)
    internal_upload_link = models.CharField(max_length=1024, null=True, blank=True)
    # upload_model = models.ForeignKey(UploadModel, on_delete=models.SET_NULL, null=True)
    uploaded_image = models.ImageField(upload_to="images/", null=True)
