# Generated by Django 3.0.7 on 2020-09-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumitai', '0015_auto_20200904_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sumitaimodel',
            name='pushuser',
            field=models.CharField(blank=True, default='F', max_length=100, null=True),
        ),
    ]
