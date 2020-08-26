from django.urls import path
from .views import RegionList,RegionDetail


urlpatterns = [
    path('RegionList/', RegionList.as_view()),
    path('RegionDetail/<int:pk>',RegionDetail.as_view()),
]
