# Generated by Django 3.1.1 on 2020-10-01 04:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('uploadingJson', '0003_auto_20201001_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsondatas',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
