# Generated by Django 4.2.2 on 2023-07-11 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0009_rename_address_donation_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='Address',
            new_name='donor_email',
        ),
        migrations.RenameField(
            model_name='donation',
            old_name='Mobile',
            new_name='donor_mobile',
        ),
        migrations.RenameField(
            model_name='donation',
            old_name='Your_name',
            new_name='donor_name',
        ),
    ]
