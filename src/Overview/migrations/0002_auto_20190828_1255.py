# Generated by Django 2.2.4 on 2019-08-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Overview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packager',
            name='phone_number',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True),
        ),
    ]
