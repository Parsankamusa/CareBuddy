# Generated by Django 4.2.2 on 2023-07-03 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('website', models.URLField()),
                ('logo', models.ImageField(upload_to='charity_logos')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_donated', models.DateTimeField(auto_now_add=True)),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charity.charity')),
            ],
        ),
    ]
