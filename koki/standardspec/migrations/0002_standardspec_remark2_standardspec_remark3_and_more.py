# Generated by Django 4.0.4 on 2022-05-23 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standardspec', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardspec',
            name='remark2',
            field=models.TextField(blank=True, null=True, verbose_name='Remark 2'),
        ),
        migrations.AddField(
            model_name='standardspec',
            name='remark3',
            field=models.TextField(blank=True, null=True, verbose_name='Remark 3'),
        ),
        migrations.AlterField(
            model_name='standardspec',
            name='remark',
            field=models.TextField(blank=True, null=True, verbose_name='Remark 1'),
        ),
        migrations.AlterField(
            model_name='standardspecline',
            name='standard_spec_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_spec', to='standardspec.standardspec'),
        ),
    ]
