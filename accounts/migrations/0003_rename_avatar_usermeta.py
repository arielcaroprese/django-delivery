# Generated by Django 4.2 on 2023-07-02 20:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_rename_account_avatar'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Avatar',
            new_name='UserMeta',
        ),
    ]
