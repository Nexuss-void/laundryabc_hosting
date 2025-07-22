from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_cashier = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username}{self.first_name}{self.last_name}'

class KategoriLayanan(models.Model):
    nama_kategori = models.CharField(max_length=50)  # Hemat, Kilat, Premium
    durasi = models.CharField(max_length=100)        # contoh: "2 hari", "1 hari", "Fleksibel < 1 hari"
    antar_jemput = models.CharField(max_length=100)  # "Tidak tersedia", "Opsional berbayar", "Gratis"
    deskripsi = models.TextField()                   # Penjelasan lengkap jika dibutuhkan

    def __str__(self):
        return self.nama_kategori

class PaketLaundry(models.Model):
    nama_paket = models.CharField(max_length=5)  # A, B, C
    deskripsi = models.CharField(max_length=200,default='-')
    layanan = models.TextField()
    harga = models.IntegerField()
    kategori = models.ForeignKey(KategoriLayanan, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.kode_paket} - {self.nama_paket}"

class Customer(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    no_telp = models.CharField(max_length=15)
    paket = models.ForeignKey(PaketLaundry, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama