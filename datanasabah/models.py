from django.db import models

# Create your models here.
class Datanasabah(models.Model):
    nama = models.CharField(max_length=50, null=True)
    alamat = models.CharField(max_length=100, null=True)
    nohp = models.CharField(max_length=15, null=True ) 
    jumlahanggota = models.CharField(max_length=3, null=True)
    waktudibuat = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama