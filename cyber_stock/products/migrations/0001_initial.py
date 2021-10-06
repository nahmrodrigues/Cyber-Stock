# Generated by Django 3.2.7 on 2021-10-06 19:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Preço')),
                ('brand', models.CharField(max_length=50, verbose_name='Marca')),
                ('batch', models.PositiveIntegerField(verbose_name='Lote')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='Descrição')),
                ('quantity_in_stock', models.PositiveIntegerField(default=0, verbose_name='Quantidade em Estoque')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nome')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Tipo de Produto',
                'verbose_name_plural': 'Tipos de Produtos',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Quantidade')),
                ('provider', models.CharField(max_length=50, verbose_name='Provedor')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='shopping_cart_product', to='products.product', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Produto no Carrinho de Compras',
                'verbose_name_plural': 'Produtos no Carrinho de Compras',
            },
        ),
        migrations.CreateModel(
            name='SalesCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Quantidade')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sales_cart_product', to='products.product', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Produto no Carrinho de Vendas',
                'verbose_name_plural': 'Produtos no Carrinho de Vendas',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_type', to='products.producttype', verbose_name='Tipo de Produto'),
        ),
    ]
