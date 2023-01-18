# Generated by Django 4.1.5 on 2023-01-18 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datanasabah', '0002_alter_datanasabah_nama'),
        ('datasampah', '0003_alter_datasampah_margin'),
        ('datapembeliansampah', '0006_datapembeliansampah_kdpembeliansampah'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datapembeliansampah',
            name='jenissampah',
        ),
        migrations.RemoveField(
            model_name='datapembeliansampah',
            name='norekening',
        ),
        migrations.AddField(
            model_name='datapembeliansampah',
            name='jenissampah',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasampah.datasampah'),
        ),
        migrations.AddField(
            model_name='datapembeliansampah',
            name='norekening',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datanasabah.datanasabah'),
        ),
    ]