# Generated by Django 3.1.2 on 2020-11-10 01:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0007_powerpointproject_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='powerpointproject',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PowerPointQuote',
        ),
    ]
