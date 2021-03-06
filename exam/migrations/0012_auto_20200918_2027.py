# Generated by Django 3.1.1 on 2020-09-18 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_auto_20200918_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='hint_1_level',
            field=models.TextField(default='', max_length=500, verbose_name='Hint in 1 level'),
        ),
        migrations.AlterField(
            model_name='student',
            name='hint_2_level',
            field=models.TextField(default='', max_length=500, verbose_name='Hint in 2 level'),
        ),
        migrations.AlterField(
            model_name='student',
            name='hint_3_level',
            field=models.TextField(default='', max_length=500, verbose_name='Hint in 3 level'),
        ),
        migrations.AlterField(
            model_name='student',
            name='hint_4_level',
            field=models.TextField(default='', max_length=500, verbose_name='Hint in 4 level'),
        ),
    ]
