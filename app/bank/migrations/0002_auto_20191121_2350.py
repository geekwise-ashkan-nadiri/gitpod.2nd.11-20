# Generated by Django 2.2.7 on 2019-11-21 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='amount',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='branch',
            name='branch_location',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='branch',
            name='branch_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_name',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bank.Account')),
            ],
        ),
    ]