# Generated by Django 4.0.2 on 2022-03-25 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_alter_analysisreport_lot_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='analysisreport',
            old_name='type',
            new_name='report_type',
        ),
    ]
