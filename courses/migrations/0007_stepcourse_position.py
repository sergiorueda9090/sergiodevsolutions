# Generated by Django 4.2.16 on 2024-09-29 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_remove_stepcourse_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='stepcourse',
            name='position',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
