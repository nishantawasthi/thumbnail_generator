from django.urls import path
from rest_api import views

urlpatterns = [
    path('', views.ThumbnailGenerator.as_view()),
    path('thumbnail_generator/', views.ThumbnailGenerator.as_view()),
]
