# Generated by Django 2.0.2 on 2018-07-04 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makeup',
            name='image',
            field=models.ImageField(upload_to='files/makeup'),
        ),
    ]
