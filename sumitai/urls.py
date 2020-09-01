from django.urls import path
from .views import Top, RegionForm, RegionList, RegionDetail, HouseList, HouseDetail, ChatCreate, Signup, Login, Request, ContractPhone, ContractView, Logout, Good


urlpatterns = [
    path('Top/', Top.as_view(), name='top'),
    path('RegionForm/', RegionForm.as_view(), name='regionform'),
    path('RegionList/', RegionList, name='regionlist'),
    path('RegionDetail/<int:pk>',RegionDetail.as_view(), name='regiondetail'),
    path('HouseList/', HouseList, name='houselist'),
    path('HouseDetail/<int:pk>', HouseDetail, name='housedetail'),
    path('ChatCreate/',ChatCreate.as_view(), name='chatcreate'),
    path('Signup/',Signup, name='signup'),
    path('Login/',Login, name='login'),
    path('Request/',Request.as_view(), name='request'),
    path('ContractPhone/', ContractPhone.as_view(), name='contractphone'),
    path('ContractView/', ContractView.as_view(), name='contractview'),
    path('Logout/', Logout, name='logout'),
    path('Good/', Good, name="good"),
]
