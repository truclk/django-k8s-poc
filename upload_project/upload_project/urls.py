"""upload_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path

from rest_framework_nested import routers

from upload_project.views import PhotoViewSet
from upload_project.views import UploadSignS3ViewSet

app_name = "upload_project"


router = routers.SimpleRouter()
router.register(r"photo", PhotoViewSet, basename="photo")
urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"upload/sign_s3", UploadSignS3ViewSet.as_view(), name="upload_sign_s3"),
]
urlpatterns += router.urls
