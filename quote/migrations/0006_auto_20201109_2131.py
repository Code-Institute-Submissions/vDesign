# Generated by Django 3.1.2 on 2020-11-09 21:31

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0005_powerpointquote_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powerpointproject',
            name='requirements',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Low', 'Check for alignment issues, fix fonts and font sizes'), ('Low', 'Change text/table to other layouts to represent better'), ('Medium', 'Use appropriate cover image and divider image'), ('Medium', 'Use appropriate images and icons/pictograms'), ('Medium', 'Add basic animations/transitions'), ('Medium', 'Convert to an interactive PDF'), ('High', 'Develop a theme/style for the document and design the document based on the theme'), ('High', 'Change layouts to high-end infographics by adding vectors/pictograms'), ('High', 'Use high-end complex animations to represent the data')], max_length=50),
        ),
    ]