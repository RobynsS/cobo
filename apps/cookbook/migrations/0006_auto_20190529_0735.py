# Generated by Django 2.2.1 on 2019-05-29 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0005_auto_20190529_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientlist',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cookbook.Unit'),
        ),
    ]
