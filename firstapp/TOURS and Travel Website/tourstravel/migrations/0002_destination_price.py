# Generated by Django 2.2.3 on 2019-08-08 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourstravel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
