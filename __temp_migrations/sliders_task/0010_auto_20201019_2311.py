# Generated by Django 2.2.4 on 2020-10-20 04:11

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('sliders_task', '0009_auto_20201019_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='slider1',
            field=otree.db.models.IntegerField(default=21, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider10',
            field=otree.db.models.IntegerField(default=48, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider2',
            field=otree.db.models.IntegerField(default=17, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider3',
            field=otree.db.models.IntegerField(default=4, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider4',
            field=otree.db.models.IntegerField(default=22, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider5',
            field=otree.db.models.IntegerField(default=50, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider6',
            field=otree.db.models.IntegerField(default=34, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider7',
            field=otree.db.models.IntegerField(default=91, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider8',
            field=otree.db.models.IntegerField(default=48, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider9',
            field=otree.db.models.IntegerField(default=14, null=True, verbose_name=''),
        ),
    ]
