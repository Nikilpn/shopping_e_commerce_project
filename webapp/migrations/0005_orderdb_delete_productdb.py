# Generated by Django 5.0.6 on 2024-06-17 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_productdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BILLINGNAME', models.CharField(blank=True, max_length=100, null=True)),
                ('BILLINGEMAIL', models.EmailField(blank=True, max_length=100, null=True)),
                ('BILLINGADDRESS', models.CharField(blank=True, max_length=100, null=True)),
                ('BILLINGPHONE', models.IntegerField(blank=True, null=True)),
                ('BILLINGPRICE', models.IntegerField(blank=True, null=True)),
                ('BILLINGMESSAGE', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='productdb',
        ),
    ]