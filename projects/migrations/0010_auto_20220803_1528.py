# Generated by Django 3.2.5 on 2022-08-03 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('projects', '0009_auto_20220803_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecthour',
            name='project',
        ),
        migrations.AlterUniqueTogether(
            name='projectmember',
            unique_together={('member', 'project')},
        ),
    ]
