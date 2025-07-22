from django.urls import path
from .views import (PaketLaundryGetPost, PaketLaundryGetUpDel,KategoriLayananGetPost,KategoriLayananGetUpDel,CustomerGetPost,CustomerGetUpDel,PaketLaundrySearchAPIView)

app_name = 'api'

urlpatterns = [
    path('paket', PaketLaundryGetPost.as_view()),            # GET all + POST
    path('paket/<int:pk>', PaketLaundryGetUpDel.as_view()),  # GET single + PUT + DELETE
    path('kategori', KategoriLayananGetPost.as_view()),            # GET all + POST
    path('kategori/<int:pk>', KategoriLayananGetUpDel.as_view()),  # GET single + PUT + DELETE   
    path('customer', CustomerGetPost.as_view()),            # GET all + POST
    path('customer/<int:pk>', CustomerGetUpDel.as_view()),  # GET single + PUT + DELETE   
    path('paket_laundry/search/', PaketLaundrySearchAPIView.as_view(), name='search-paket-laundry'),
]
