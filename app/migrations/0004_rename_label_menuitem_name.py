# Generated by Django 4.2.3 on 2023-08-11 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_menuitem_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='label',
            new_name='name',
        ),
    ]
