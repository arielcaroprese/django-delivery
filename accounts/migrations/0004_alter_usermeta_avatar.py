# Generated by Django 4.2 on 2023-07-03 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_avatar_usermeta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermeta',
            name='avatar',
            field=models.ImageField(blank=True, default='delivery_app/static/delivery_app/assets/img/avatar.jpg', null=True, upload_to='avatars'),
        ),
    ]