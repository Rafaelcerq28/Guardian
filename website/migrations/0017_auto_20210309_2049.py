# Generated by Django 2.1 on 2021-03-09 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20210308_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='cnpj',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]