# Generated by Django 4.2 on 2023-05-10 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_query_number_join_query_prefix_algo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='query',
            old_name='execution_energy',
            new_name='execution_energy_hybrid',
        ),
        migrations.AddField(
            model_name='query',
            name='execution_energy_pg',
            field=models.FloatField(null=True),
        ),
    ]
