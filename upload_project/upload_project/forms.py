from django import forms

from upload_project.models import PhotoModel


class UploadForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = ["upload_type", "surname", "firstname", "donate_type", "description", "uploaded_image"]
