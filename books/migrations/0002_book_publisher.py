# Generated by Django 4.2 on 2023-06-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank='True', max_length=64, null='True', verbose_name='Издательство'),
            preserve_default='True',
        ),
    ]
