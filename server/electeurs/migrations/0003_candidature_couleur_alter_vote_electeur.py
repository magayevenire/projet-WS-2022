# Generated by Django 4.1.2 on 2022-10-28 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('electeurs', '0002_alter_vote_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidature',
            name='couleur',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='electeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='electeur_votes', to='electeurs.electeur'),
        ),
    ]
