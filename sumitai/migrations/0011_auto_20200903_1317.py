# Generated by Django 3.0.7 on 2020-09-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumitai', '0010_auto_20200902_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sumitaimodel',
            name='read',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sumitaimodel',
            name='readtext',
            field=models.CharField(blank=True, default='a', max_length=100, null=True),
        ),
    ]