# Generated by Django 3.1.1 on 2020-09-18 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20200918_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='key',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Last 4 number of phone'),
        ),
    ]
