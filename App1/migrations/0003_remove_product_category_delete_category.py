# Generated by Django 4.1.5 on 2023-01-14 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_category_product_price_alter_product_disc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
