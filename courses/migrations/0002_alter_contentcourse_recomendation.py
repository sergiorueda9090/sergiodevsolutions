# Generated by Django 4.2.16 on 2024-09-29 15:13

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentcourse',
            name='recomendation',
            field=tinymce.models.HTMLField(),
        ),
    ]
