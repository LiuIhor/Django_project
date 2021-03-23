# Generated by Django 3.1.7 on 2021-03-15 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210314_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='created_by_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.users', verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
