# Generated by Django 4.0.5 on 2022-07-04 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_moto'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='about',
            field=models.TextField(null=True, verbose_name='Car about'),
        ),
    ]