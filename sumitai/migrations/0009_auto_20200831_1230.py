# Generated by Django 3.0.7 on 2020-08-31 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumitai', '0008_sumitaimodel_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='sumitaimodel',
            name='good',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sumitaimodel',
            name='read',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sumitaimodel',
            name='readtext',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
