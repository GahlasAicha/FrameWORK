from django.urls import path
from . import views

urlpatterns = [
    path("", views.about, name="about"),
    path('collection/<int:n>/', views.collection_detail, name='collection_detail')
]