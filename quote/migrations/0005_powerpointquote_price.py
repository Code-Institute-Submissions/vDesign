# Generated by Django 3.1.2 on 2020-11-09 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0004_remove_powerpointquote_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='powerpointquote',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
