# Generated by Django 4.2 on 2023-05-14 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_remove_query_prefix_search_energy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='json_plan_hinter',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='json_plan_pg',
            field=models.TextField(null=True),
        ),
    ]