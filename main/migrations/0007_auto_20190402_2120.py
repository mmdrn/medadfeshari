# Generated by Django 2.1.5 on 2019-04-02 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190402_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='myidea',
            name='idea_publisher',
            field=models.CharField(default='هم مدادفشاری', max_length=200, verbose_name='Publisher'),
        ),
        migrations.AlterField(
            model_name='myidea',
            name='idea_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 2, 21, 20, 38, 344623), verbose_name='date published'),
        ),
    ]
