# Generated by Django 5.0.6 on 2024-05-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATEGORY', models.CharField(blank=True, max_length=100, null=True)),
                ('PRODUCTNAME', models.CharField(blank=True, max_length=100, null=True)),
                ('PRODUCTDESCRIPTION', models.CharField(blank=True, max_length=100, null=True)),
                ('CATEGORYIMAGE', models.ImageField(blank=True, null=True, upload_to='productimages')),
            ],
        ),
    ]