# Generated by Django 2.2.4 on 2020-10-20 04:28

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('sliders_task', '0017_auto_20201019_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='slider1',
            field=otree.db.models.IntegerField(default=82, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider10',
            field=otree.db.models.IntegerField(default=33, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider2',
            field=otree.db.models.IntegerField(default=21, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider3',
            field=otree.db.models.IntegerField(default=66, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider4',
            field=otree.db.models.IntegerField(default=4, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider5',
            field=otree.db.models.IntegerField(default=92, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider6',
            field=otree.db.models.IntegerField(default=9, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider7',
            field=otree.db.models.IntegerField(default=4, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider8',
            field=otree.db.models.IntegerField(default=39, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider9',
            field=otree.db.models.IntegerField(default=86, null=True, verbose_name=''),
        ),
    ]
