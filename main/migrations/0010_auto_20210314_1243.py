# Generated by Django 3.1.7 on 2021-03-14 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210314_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='role_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.roles', verbose_name='role'),
        ),
    ]
