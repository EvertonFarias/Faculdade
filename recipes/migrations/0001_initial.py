# Generated by Django 4.2.7 on 2023-11-19 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemListaCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField(default=1)),
            ],
        ),
    ]
