# Generated by Django 3.1.2 on 2020-11-15 01:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolio_paragraph'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
