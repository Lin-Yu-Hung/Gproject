# Generated by Django 3.2.8 on 2022-09-24 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_cartdb_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='chip',
            field=models.IntegerField(default=''),
        ),
    ]