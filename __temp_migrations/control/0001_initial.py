# Generated by Django 2.2.4 on 2020-05-12 17:16

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='control_group', to='otree.Session')),
            ],
            options={
                'db_table': 'control_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='control_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'control_subsession',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('decision', otree.db.models.StringField(choices=[('A', 'A'), ('B', 'B')], max_length=10000, null=True)),
                ('question_1', otree.db.models.IntegerField(null=True, verbose_name='假设你是第一人并且选择了B，在第二人也选择B的情况下你获得的点数是：')),
                ('question_2', otree.db.models.IntegerField(null=True, verbose_name='假设你是第二人并且选择了B，在第一人选择A的情况下你获得的点数是：')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='control.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='control_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='control_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.Subsession')),
            ],
            options={
                'db_table': 'control_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.Subsession'),
        ),
    ]
