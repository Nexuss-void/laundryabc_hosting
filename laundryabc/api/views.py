from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView
from django.http import HttpResponse

from laundryabc_app.models import PaketLaundry,KategoriLayanan,Customer
from api.serializers import PaketLaundrySerializer, KategoriLayananSerializer, CustomerSerializer

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')

class PaketLaundryGetPost(ListCreateAPIView):
    queryset = PaketLaundry.objects.all()
    serializer_class = PaketLaundrySerializer

class PaketLaundryGetUpDel(RetrieveUpdateDestroyAPIView):
    queryset = PaketLaundry.objects.all()
    serializer_class = PaketLaundrySerializer

class KategoriLayananGetPost(ListCreateAPIView):
    queryset = KategoriLayanan.objects.all()
    serializer_class = KategoriLayananSerializer

class KategoriLayananGetUpDel(RetrieveUpdateDestroyAPIView):
    queryset = KategoriLayanan.objects.all()
    serializer_class = KategoriLayananSerializer

class CustomerGetPost(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerGetUpDel(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class PaketLaundrySearchAPIView(ListAPIView):
    serializer_class = PaketLaundrySerializer

    def get_queryset(self):
        query = self.request.query_params.get('search', '')
        if query:
            return PaketLaundry.objects.filter(nama_paket__icontains=query)
        return PaketLaundry.objects.all()