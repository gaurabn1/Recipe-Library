# Generated by Django 5.0.6 on 2024-05-25 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(upload_to='Recipe_images'),
        ),
    ]
