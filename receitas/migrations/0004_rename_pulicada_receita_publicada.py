# Generated by Django 3.2.9 on 2021-11-12 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_receita_pulicada'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='pulicada',
            new_name='publicada',
        ),
    ]
