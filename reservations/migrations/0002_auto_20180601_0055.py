# Generated by Django 2.0.4 on 2018-05-31 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artistetypeshow',
            options={'managed': False, 'verbose_name_plural': 'Artiste Type de Spéctacles'},
        ),
        migrations.AlterModelOptions(
            name='artists',
            options={'managed': False, 'verbose_name': 'Artiste', 'verbose_name_plural': 'Artistes'},
        ),
        migrations.AlterModelOptions(
            name='localities',
            options={'managed': False, 'verbose_name': 'Localité', 'verbose_name_plural': 'Localités'},
        ),
        migrations.AlterModelOptions(
            name='locations',
            options={'managed': False, 'verbose_name': 'Emplacement', 'verbose_name_plural': 'Emplacements'},
        ),
        migrations.AlterModelOptions(
            name='representations',
            options={'managed': False, 'verbose_name': 'Representation', 'verbose_name_plural': 'Representations'},
        ),
        migrations.AlterModelOptions(
            name='shows',
            options={'managed': False, 'verbose_name': 'Spéctacle', 'verbose_name_plural': 'Spéctacles'},
        ),
        migrations.AlterModelOptions(
            name='types',
            options={'managed': False, 'verbose_name': 'Type', 'verbose_name_plural': 'Types'},
        ),
    ]