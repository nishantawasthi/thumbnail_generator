from django.urls import path
from django.conf.urls.static import  static

from rest_api import views
from thumbnail_generator import settings

urlpatterns = [
    path('', views.ThumbnailGenerator.as_view()),
    path('thumbnail_generator/', views.ThumbnailGenerator.as_view()),
    path('thumbnail_generator/<str:task_id>',
         views.ThumbnailGenerator.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
