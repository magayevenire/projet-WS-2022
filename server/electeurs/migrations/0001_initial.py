# Generated by Django 4.1.2 on 2022-10-23 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('circonscriptions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('elections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Electeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_cni', models.CharField(max_length=50, unique=True)),
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
                ('prenom', models.CharField(blank=True, max_length=50, null=True)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('adresse', models.CharField(blank=True, max_length=250, null=True)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('modifier', models.DateTimeField(auto_now=True)),
                ('bureau_vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscrits', to='circonscriptions.bureau')),
                ('user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electeur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Candidature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_parti', models.CharField(blank=True, max_length=50, null=True)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('modifier', models.DateTimeField(auto_now=True)),
                ('candidat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidatures', to='electeurs.electeur')),
                ('election', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidats', to='elections.election')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('modifier', models.DateTimeField(auto_now=True)),
                ('bureau_vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suffrages', to='circonscriptions.bureau')),
                ('candidature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote', to='electeurs.candidature')),
                ('electeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electeurs.electeur')),
            ],
            options={
                'unique_together': {('electeur', 'candidature')},
            },
        ),
    ]
