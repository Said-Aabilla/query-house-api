# Generated by Django 4.2 on 2023-04-25 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='JoinAlgorithm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='JoinIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projection', models.CharField(max_length=255)),
                ('all', models.BooleanField(null=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projections', to='app.attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=500)),
                ('join_order', models.CharField(max_length=250)),
                ('execution_time', models.FloatField(null=True)),
                ('estimated_execution_time', models.FloatField(null=True)),
                ('execution_energy', models.FloatField(null=True)),
                ('joins', models.ManyToManyField(to='app.join')),
                ('projections', models.ManyToManyField(to='app.projection')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selection', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SelectionAlgorithm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='app.domain')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('alias', models.CharField(max_length=50)),
                ('queries', models.ManyToManyField(to='app.query')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SelectionOperator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.operator')),
                ('selection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.selection')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selectionOperators', to='app.value')),
            ],
        ),
        migrations.AddField(
            model_name='selection',
            name='algorithm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selections', to='app.selectionalgorithm'),
        ),
        migrations.AddField(
            model_name='selection',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selections', to='app.attribute'),
        ),
        migrations.AddField(
            model_name='selection',
            name='operators',
            field=models.ManyToManyField(through='app.SelectionOperator', to='app.operator'),
        ),
        migrations.AddField(
            model_name='selection',
            name='queries',
            field=models.ManyToManyField(to='app.query'),
        ),
        migrations.AddField(
            model_name='query',
            name='selections',
            field=models.ManyToManyField(to='app.selection'),
        ),
        migrations.AddField(
            model_name='query',
            name='tables',
            field=models.ManyToManyField(to='app.table'),
        ),
        migrations.AddField(
            model_name='projection',
            name='queries',
            field=models.ManyToManyField(to='app.query'),
        ),
        migrations.CreateModel(
            name='JoinAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=20)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.attribute')),
                ('join', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.join')),
            ],
        ),
        migrations.AddField(
            model_name='join',
            name='algorithm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joins', to='app.joinalgorithm'),
        ),
        migrations.AddField(
            model_name='join',
            name='index',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joins', to='app.joinindex'),
        ),
        migrations.AddField(
            model_name='join',
            name='queries',
            field=models.ManyToManyField(to='app.query'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='app.table'),
        ),
        migrations.CreateModel(
            name='Aggregation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function', models.CharField(max_length=255)),
                ('projection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aggregations', to='app.projection')),
            ],
        ),
    ]
