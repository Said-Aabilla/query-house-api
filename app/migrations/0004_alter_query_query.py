# Generated by Django 4.2 on 2023-04-25 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_projection_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query',
            field=models.TextField(),
        ),
    ]