# Generated by Django 3.1.1 on 2020-09-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20200918_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='hint_next_level',
            field=models.CharField(default='', max_length=500, verbose_name='Hint for next level'),
        ),
    ]
