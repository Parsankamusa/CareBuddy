# Generated by Django 4.2.2 on 2023-07-06 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0005_donation_delete_fooddonation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='category',
            field=models.ManyToManyField(related_name='item', to='charity.category'),
        ),
    ]
