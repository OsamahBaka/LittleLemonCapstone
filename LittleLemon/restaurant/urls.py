from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    #path('booking/', views.BookingList.as_view(), name='BookingList'),
    path('items/', views.MenuList.as_view(), name='MenuList'),
    path('items/<int:pk>', views.MenuItemDetail.as_view(), name='MenuItemDetail'),
]
