# Generated by Django 3.1.2 on 2020-11-14 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='paragraph',
            field=models.TextField(default='paragraph'),
        ),
    ]
