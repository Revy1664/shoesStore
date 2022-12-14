# Generated by Django 4.1.3 on 2022-12-03 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('logo', models.ImageField(default='static/images/default_for_brand.jpg', upload_to='logos/')),
            ],
        ),
    ]
