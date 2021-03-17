# Generated by Django 2.1 on 2021-03-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20210218_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_mov', models.CharField(choices=[('entrada', 'Entrada'), ('saida', 'Saida')], max_length=7)),
                ('quantidade', models.IntegerField()),
                ('data', models.CharField(max_length=255)),
                ('numero_nf', models.IntegerField()),
            ],
        ),
    ]
