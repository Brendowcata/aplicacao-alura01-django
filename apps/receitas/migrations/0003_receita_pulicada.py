# Generated by Django 3.2.9 on 2021-11-07 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_receita_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='pulicada',
            field=models.BooleanField(default=False),
        ),
    ]
