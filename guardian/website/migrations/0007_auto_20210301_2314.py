# Generated by Django 2.1 on 2021-03-02 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20210301_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacoes',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]