from django.db import models
from datanasabah.models import Datanasabah 
from databukutabungan.models import Databukutabungan
from datasampah.models import Datasampah

class Datapembeliansampah(models.Model):
    kdpembeliansampah = models.CharField(max_length=4, null=True)
    norekening = models.ForeignKey(Databukutabungan(), on_delete=models.CASCADE, null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)
    jenissampah = models.ForeignKey(Datasampah(), on_delete=models.CASCADE, null=True)
    berat = models.IntegerField()
    jumlah = models.IntegerField(null=True)

    def __str__(self):
        return self.kdpembeliansampah
