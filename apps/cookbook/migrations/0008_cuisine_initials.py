# Generated by Django 2.2.1 on 2019-06-07 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0007_auto_20190529_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuisine',
            name='initials',
            field=models.CharField(default='be', max_length=2),
            preserve_default=False,
        ),
    ]