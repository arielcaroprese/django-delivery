# Generated by Django 4.2 on 2023-07-02 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0011_rename_product_id_reviews_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category_id',
            new_name='category',
        ),
    ]
