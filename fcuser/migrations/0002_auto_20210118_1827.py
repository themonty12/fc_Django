# Generated by Django 3.1.2 on 2021-01-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcuser',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='등록날짜'),
        ),
    ]
