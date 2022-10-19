# Generated by Django 4.1.2 on 2022-10-18 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('position_geographique', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'unique_together': {('nom',)},
            },
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('position_geographique', models.CharField(blank=True, max_length=100, null=True)),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departements', to='circonscriptions.region')),
            ],
            options={
                'unique_together': {('nom', 'region')},
            },
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('position_geographique', models.CharField(blank=True, max_length=100, null=True)),
                ('departement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communes', to='circonscriptions.departement')),
            ],
            options={
                'unique_together': {('nom', 'departement')},
            },
        ),
        migrations.CreateModel(
            name='Bureau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('commune', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bureaux', to='circonscriptions.commune')),
            ],
            options={
                'unique_together': {('commune', 'numero')},
            },
        ),
    ]
