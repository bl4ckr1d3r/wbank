# Generated by Django 4.1.5 on 2023-01-18 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datapembeliansampah', '0003_remove_datapembeliansampah_kdpembeliansampah'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datapembeliansampah',
            name='nama',
        ),
        migrations.AddField(
            model_name='datapembeliansampah',
            name='kdpembeliansampah',
            field=models.CharField(max_length=4, null=True),
        ),
    ]