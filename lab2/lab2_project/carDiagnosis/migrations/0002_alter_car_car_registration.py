# Generated by Django 4.1.3 on 2022-12-24 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carDiagnosis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_registration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carDiagnosis.owner'),
        ),
    ]
