# Generated by Django 4.1.2 on 2022-10-23 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('circonscriptions', '0003_alter_commune_nom_alter_departement_nom_and_more'),
        ('electeurs', '0010_rename_canditure_vote_candidature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electeur',
            name='bureau_vote',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='inscrits', to='circonscriptions.bureau'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='electeur',
            name='numero_cni',
            field=models.CharField(default=5, max_length=50),
            preserve_default=False,
        ),
    ]
