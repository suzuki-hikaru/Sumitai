from django.urls import path
from .views import Top, RegionForm, RegionList, RegionDetail, HouseList, HouseDetail, ChatCreate, Signup, Login, Request, ContractPhone, ContractView, Logout


urlpatterns = [
    path('Top/', Top.as_view(), name='top'),
    path('RegionForm/', RegionForm.as_view(), name='regionform'),
    path('RegionList/', RegionList, name='regionlist'),
    path('RegionDetail/<int:pk>',RegionDetail.as_view(), name='regiondetail'),
    path('HouseList/', HouseList.as_view(), name='houselist'),
    path('HouseDetail/', HouseDetail.as_view(), name='housedetail'),
    path('ChatCreate/',ChatCreate.as_view(), name='chatcreate'),
    path('Signup/',Signup, name='signup'),
    path('Login/',Login, name='login'),
    path('Request/',Request.as_view(), name='request'),
    path('ContractPhone/', ContractPhone.as_view(), name='contractphone'),
    path('ContractView/', ContractView.as_view(), name='contractview'),
    path('Logout/', Logout, name='logout')
]
