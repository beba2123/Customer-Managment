# Generated by Django 4.2.4 on 2023-08-30 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acounts', '0010_alter_customer_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phone_number',
        ),
    ]