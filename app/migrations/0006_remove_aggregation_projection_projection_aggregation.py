# Generated by Django 4.2 on 2023-04-25 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_join_algorithm_alter_join_index_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aggregation',
            name='projection',
        ),
        migrations.AddField(
            model_name='projection',
            name='aggregation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projections', to='app.aggregation'),
            preserve_default=False,
        ),
    ]
