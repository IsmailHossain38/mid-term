# Generated by Django 5.0 on 2023-12-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carmodel', '0003_carmodel_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='image_field',
            field=models.ImageField(blank=True, null=True, upload_to='carmodel/media/uploads/'),
        ),
    ]