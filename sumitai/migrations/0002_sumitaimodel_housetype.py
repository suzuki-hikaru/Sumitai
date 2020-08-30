# Generated by Django 3.0.7 on 2020-08-27 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumitai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sumitaimodel',
            name='houseType',
            field=models.CharField(choices=[('マンション', 'マンション（選択）'), ('アパート', 'アパート（選択）'), ('一軒家', '一軒家（選択）')], max_length=100, null=True),
        ),
    ]