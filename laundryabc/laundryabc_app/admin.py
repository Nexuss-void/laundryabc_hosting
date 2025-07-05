from django.contrib import admin
from .models import PaketLaundry,User

admin.site.register(User)
# Registrasi model agar muncul di halaman admin
admin.site.register(PaketLaundry)

# Kustomisasi tampilan halaman admin
admin.site.site_header = "Admin Laundry"
admin.site.site_title = "Dashboard Admin Laundry"
admin.site.index_title = "Selamat Datang di Panel Admin Laundry"
