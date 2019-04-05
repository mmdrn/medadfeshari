# Generated by Django 2.1.5 on 2019-04-02 20:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_auto_20190402_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='myidea',
            name='created_by',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myidea',
            name='idea_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 2, 20, 58, 35, 462491), verbose_name='date published'),
        ),
    ]
