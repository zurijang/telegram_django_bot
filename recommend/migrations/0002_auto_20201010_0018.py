# Generated by Django 3.0.10 on 2020-10-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='link',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='province',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='state',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='type1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='type2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='type3',
            field=models.CharField(max_length=100),
        ),
    ]