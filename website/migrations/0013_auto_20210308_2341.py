# Generated by Django 2.1 on 2021-03-09 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_movimentacoes_clientes'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='cnpj',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientes',
            name='telefone',
            field=models.IntegerField(default=1111, max_length=9),
            preserve_default=False,
        ),
    ]
