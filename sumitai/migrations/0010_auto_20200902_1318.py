# Generated by Django 3.0.7 on 2020-09-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumitai', '0009_auto_20200831_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sumitaimodel',
            name='good',
            field=models.IntegerField(default=0),
        ),
    ]
