# Generated by Django 3.2.4 on 2021-06-26 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imgP',
            field=models.ImageField(null=True, upload_to='productos', verbose_name='Imagen producto'),
        ),
    ]
