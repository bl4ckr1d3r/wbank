from django.db import models
from databukutabungan.models import Databukutabungan

# Create your models here.
class Datapenarikan(models.Model):
    norekening = models.ForeignKey(Databukutabungan(), on_delete=models.CASCADE, null=True)
    jumlah = models.IntegerField()
    keterangan = models.CharField(max_length=100, null=True)
    waktudibuat = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.keterangan