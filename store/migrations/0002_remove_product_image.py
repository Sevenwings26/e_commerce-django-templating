# Generated by Django 4.2.16 on 2024-10-14 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="image",),
    ]
