# Generated by Django 3.2.5 on 2022-08-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20220801_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecthour',
            name='period',
        ),
        migrations.AddField(
            model_name='projecthour',
            name='week',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
