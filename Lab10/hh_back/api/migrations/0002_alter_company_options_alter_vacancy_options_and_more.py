# Generated by Django 5.0.4 on 2024-04-10 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['salary'], 'verbose_name': 'Vacancy', 'verbose_name_plural': 'Vacancies'},
        ),
        migrations.AlterUniqueTogether(
            name='company',
            unique_together={('name', 'city', 'address')},
        ),
        migrations.AlterIndexTogether(
            name='company',
            index_together={('name', 'city', 'address')},
        ),
        migrations.AlterModelTable(
            name='company',
            table='company',
        ),
    ]
