# Generated by Django 2.2.7 on 2019-11-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='type',
            field=models.CharField(choices=[('1', '요가/필라테스'), ('2', '요가'), ('3', '필라테스')], default='1', max_length=1, verbose_name='센터 종류'),
        ),
    ]
