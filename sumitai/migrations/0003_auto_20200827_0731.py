# Generated by Django 3.0.7 on 2020-08-27 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sumitai', '0002_sumitaimodel_housetype'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='sumitaimodel',
            name='region',
            field=models.CharField(choices=[('長野県', '長野県'), ('千葉県', '千葉県'), ('兵庫県', '兵庫県'), ('岡山県', '岡山県'), ('三重県', '三重県')], max_length=100, null=True),
        ),
    ]