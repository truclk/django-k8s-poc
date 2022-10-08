from __future__ import absolute_import

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic.edit import FormView

from rest_framework.viewsets import ModelViewSet

from upload_project.forms import UploadForm
from upload_project.models import PhotoModel
from upload_project.serializers import PhotoSerializer


class PhotoViewSet(ModelViewSet):
    queryset = PhotoModel.objects.all()
    serializer_class = PhotoSerializer


def photo_image_view(request):

    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = UploadForm()
    return render(request, "upload_form.html", {"form": form})


def success(request):
    return render(request, "success.html")


def index(request):
    if request.method == "GET":
        photos = PhotoModel.objects.all()
        return render(request, "photo_models.html", {"photo_images": photos})
