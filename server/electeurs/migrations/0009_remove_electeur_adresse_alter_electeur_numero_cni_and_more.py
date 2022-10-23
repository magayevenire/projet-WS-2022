# Generated by Django 4.1.2 on 2022-10-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electeurs', '0008_rename_canditaure_vote_canditure'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electeur',
            name='Adresse',
        ),
        migrations.AlterField(
            model_name='electeur',
            name='numero_cni',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='electeur',
            name='adresse',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
