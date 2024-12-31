# Generated by Django 5.1.4 on 2024-12-31 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PricingPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('period', models.CharField(max_length=50, verbose_name='Período')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('title_btn', models.CharField(max_length=50, verbose_name='Texto do Botão')),
                ('link_btn', models.URLField(verbose_name='Link do Botão')),
                ('situation', models.BooleanField(default=True, verbose_name='Situação')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Destaque')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de edição')),
            ],
            options={
                'verbose_name': 'Plano de Preço',
                'verbose_name_plural': 'Planos de Preços',
            },
        ),
    ]
