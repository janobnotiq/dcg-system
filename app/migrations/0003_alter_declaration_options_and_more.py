# Generated by Django 5.1.1 on 2024-09-25 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_declaration_number_gtd_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='declaration',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AlterField(
            model_name='declaration',
            name='date_recorded',
            field=models.DateField(verbose_name='qayd etilgan sana'),
        ),
    ]
