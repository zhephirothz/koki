# Generated by Django 4.0.4 on 2022-05-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standardspec', '0005_alter_standardspecline_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardspecline',
            name='name',
            field=models.CharField(max_length=10, verbose_name='name'),
        ),
    ]
