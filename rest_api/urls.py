from django.urls import path
from rest_api import views

urlpatterns = [
    path('thumbnail_generator/', views.ThumbnailGenerator.as_view()),
]
