# Generated by Django 2.1 on 2021-03-11 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_auto_20210310_2231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientes',
            options={},
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='movimentacoes',
        ),
        migrations.AddField(
            model_name='movimentacoes',
            name='clientes',
            field=models.ManyToManyField(to='website.Clientes'),
        ),
    ]
