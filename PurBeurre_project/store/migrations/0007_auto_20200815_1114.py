# Generated by Django 3.0.7 on 2020-08-15 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200815_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attributs',
            old_name='name_person',
            new_name='auth_user',
        ),
    ]
