# Generated by Django 2.1.7 on 2019-03-26 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0002_auto_20190326_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='ingredient0',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drink',
            name='ingredient1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drink',
            name='ingredient2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drink',
            name='ingredient3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drink',
            name='ingredient4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drink',
            name='ingredient5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drink',
            name='ingredient6',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drink',
            name='ingredient7',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
