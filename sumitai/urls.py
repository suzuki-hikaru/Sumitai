from django.urls import path
from .views import RegionList,RegionDetail,ChatCreate


urlpatterns = [
    path('RegionList/', RegionList.as_view(), name='list'),
    path('RegionDetail/<int:pk>',RegionDetail.as_view(), name='detail'),
    path('ChatCreate/',ChatCreate.as_view(), name='chat'),
]
