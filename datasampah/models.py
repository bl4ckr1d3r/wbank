from django.db import models

# Create your models here.
class Datasampah(models.Model):
    JENISSAMPAH = (
        ('Gelas Bening', 'Gelas Bening'),
        ('Gelas Warna', 'Gelas Warna'),
        ('Botol Bekas', 'Botol Bening'),
        ('Botol Warna', 'Botol Warna'),
        ('Plastik', 'Plastik'),
        ('Besi', 'Besi'),
        ('Kardus', 'Kardus'),
    )
    jenissampah = models.CharField(max_length=15, choices=JENISSAMPAH)
    hargajual = models.IntegerField()
    hargabeli = models.IntegerField()
    margin = models.IntegerField(null=True)
    waktudibuat = models.DateTimeField(auto_now_add=True, null=True)  

    def __str__(self):
        return self.jenissampah
