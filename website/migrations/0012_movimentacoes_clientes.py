# Generated by Django 2.1 on 2021-03-09 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_clientes'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimentacoes',
            name='clientes',
            field=models.ManyToManyField(to='website.Clientes'),
        ),
    ]
