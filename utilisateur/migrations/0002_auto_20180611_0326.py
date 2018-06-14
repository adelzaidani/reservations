# Generated by Django 2.0.4 on 2018-06-11 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='utilisateur.Role'),
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(default='Client', max_length=30),
        ),
    ]
