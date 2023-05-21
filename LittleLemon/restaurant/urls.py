from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('', views.index, name='index'),
    # path('booking/', views.BookingList.as_view(), name='BookingList'),
    path('menu/items/', views.MenuList.as_view(), name='MenuList'),
    path('menu/items/<int:pk>', views.MenuItemDetail.as_view(), name='MenuItemDetail'),
    path('api-token-auth/', obtain_auth_token),
]
