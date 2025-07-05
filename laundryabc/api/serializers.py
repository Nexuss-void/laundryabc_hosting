from rest_framework import serializers
from laundryabc_app.models import PaketLaundry, KategoriLayanan, Customer

class PaketLaundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaketLaundry
        fields = '__all__'

class KategoriLayananSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriLayanan
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'