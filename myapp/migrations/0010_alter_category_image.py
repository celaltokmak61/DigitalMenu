# Generated by Django 3.2.13 on 2023-04-04 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='noimage.png', upload_to='category_images'),
        ),
    ]
