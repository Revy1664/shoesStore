# Generated by Django 4.1.3 on 2022-12-03 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Бренд', 'verbose_name_plural': 'Бренды'},
        ),
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(default='static/images/default_for_brand.jpg', upload_to='logos/', verbose_name='Логотип'),
        ),
    ]
