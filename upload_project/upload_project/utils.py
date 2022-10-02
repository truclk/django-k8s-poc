from upload_project.models import UploadModel


def confirm_upload(file_path):
    upload_model = UploadModel.objects.filter(file_path=file_path).first()
    if upload_model:
        # If this is a link outside system do not save this url
        upload_model.status = UploadModel.STATUS_UPLOADED
        upload_model.save(update_fields=["status"])
        return file_path, upload_model.id
