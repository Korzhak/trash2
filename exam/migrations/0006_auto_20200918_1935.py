# Generated by Django 3.1.1 on 2020-09-18 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_student_hint_next_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='hint_next_level',
        ),
        migrations.AddField(
            model_name='student',
            name='hint_1_level',
            field=models.CharField(default='', max_length=500, verbose_name='Hint in 1 level'),
        ),
        migrations.AddField(
            model_name='student',
            name='hint_2_level',
            field=models.CharField(default='', max_length=500, verbose_name='Hint in 2 level'),
        ),
        migrations.AddField(
            model_name='student',
            name='hint_3_level',
            field=models.CharField(default='', max_length=500, verbose_name='Hint in 3 level'),
        ),
    ]