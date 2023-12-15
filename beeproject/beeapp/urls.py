from django.urls import path
from .views import file_upload, file_list, file_download

urlpatterns = [
path('upload/', file_upload, name='file_upload'),
path('list/', file_list, name='file_list'),
path('download/<int:file_id>/', file_download, name='file_download'),
]