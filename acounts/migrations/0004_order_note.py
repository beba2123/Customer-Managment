# Generated by Django 4.2.3 on 2023-08-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acounts', '0003_tags_product_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
