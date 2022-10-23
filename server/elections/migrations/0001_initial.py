# Generated by Django 4.1.2 on 2022-10-23 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periode_inscription_debut', models.DateField(blank=True, null=True)),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('periode_inscription_fin', models.DateField(blank=True, null=True)),
                ('periode_depot_canditature_debut', models.DateField(blank=True, null=True)),
                ('periode_depot_canditature_fin', models.DateField(blank=True, null=True)),
                ('jour_vote', models.DateField(blank=True, null=True)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('modifier', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
