# Generated by Django 5.1.2 on 2024-10-23 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_rename_id_district_district_district_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='district',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='district',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='District',
        ),
    ]
