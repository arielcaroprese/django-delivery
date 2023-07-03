# Generated by Django 4.2 on 2023-07-01 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0004_products_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='delivery_app.categories'),
        ),
    ]
