# Generated by Django 2.2.4 on 2019-08-28 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Overview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packager',
            name='size_not_match',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
