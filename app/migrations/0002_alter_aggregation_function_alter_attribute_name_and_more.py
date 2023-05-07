# Generated by Django 4.2 on 2023-04-25 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aggregation',
            name='function',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='joinalgorithm',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='joinindex',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='operator',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='query',
            name='join_order',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='selectionalgorithm',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='alias',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
