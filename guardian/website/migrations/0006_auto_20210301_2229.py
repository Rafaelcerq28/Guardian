# Generated by Django 2.1 on 2021-03-02 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20210301_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacoes',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
