from django.db import models
from datanasabah.models import Datanasabah
# Create your models here.

class Databukutabungan(models.Model):
    nama = models.ForeignKey(Datanasabah(), on_delete=models.CASCADE, null=True)
    noidentitas = models.CharField(max_length=25, null=True)
    norekening = models.CharField(max_length=9, null=True)
    cabang = models.CharField(max_length=50, null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)
    saldonominal = models.IntegerField(null=True)
    saldoemas = models.IntegerField(null=True)

    def __str__(self):
        return self.norekening