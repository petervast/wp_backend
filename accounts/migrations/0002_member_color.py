# Generated by Django 3.2.5 on 2022-08-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='color',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]