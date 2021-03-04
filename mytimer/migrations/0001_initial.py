# Generated by Django 3.1.7 on 2021-03-03 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.PositiveIntegerField(verbose_name='Timer start')),
                ('end', models.PositiveIntegerField(verbose_name='Timer end')),
            ],
            options={
                'verbose_name': 'Timer',
                'verbose_name_plural': 'Timers',
            },
        ),
    ]