# Generated by Django 4.1.7 on 2023-03-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvcard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]