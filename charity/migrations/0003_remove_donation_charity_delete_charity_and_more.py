# Generated by Django 4.2.2 on 2023-07-04 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0002_auto_20230704_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='charity',
        ),
        migrations.DeleteModel(
            name='Charity',
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
    ]
