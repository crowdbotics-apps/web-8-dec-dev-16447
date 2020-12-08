# Generated by Django 2.2.17 on 2020-12-08 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=20, unique=True)),
                ('card_exp_month', models.CharField(blank=True, max_length=2)),
                ('card_exp_year', models.CharField(blank=True, max_length=4)),
                ('card_cvv', models.CharField(blank=True, max_length=4)),
                ('card_security_code', models.CharField(blank=True, max_length=4)),
            ],
        ),
    ]