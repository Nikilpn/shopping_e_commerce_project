# Generated by Django 5.0.6 on 2024-05-13 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_productdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdb',
            old_name='CATEGORYIMAGE',
            new_name='PRODUCTIMAGE',
        ),
    ]
