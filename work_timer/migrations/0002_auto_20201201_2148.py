# Generated by Django 2.2.16 on 2020-12-02 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_timer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
