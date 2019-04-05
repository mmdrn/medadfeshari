# Generated by Django 2.1.5 on 2019-04-02 20:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190402_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='myidea',
            name='idea_publisher',
            field=models.CharField(default='kia', max_length=200, verbose_name='Publisher'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myidea',
            name='idea_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 2, 20, 17, 32, 258367), verbose_name='date published'),
        ),
    ]
