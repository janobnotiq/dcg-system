# Generated by Django 5.1.1 on 2024-09-25 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_declaration_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='updated_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='declaration',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
