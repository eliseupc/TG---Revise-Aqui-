# Generated by Django 3.1 on 2020-08-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultor', '0002_servico_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='valor_servico',
            field=models.CharField(blank=True, max_length=100, verbose_name='Valor Serviço'),
        ),
    ]