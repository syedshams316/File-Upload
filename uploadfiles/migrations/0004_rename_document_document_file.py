# Generated by Django 3.2.13 on 2022-05-01 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploadfiles', '0003_remove_document_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='document',
            new_name='file',
        ),
    ]