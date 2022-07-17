# Generated by Django 4.0.6 on 2022-07-17 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(help_text='Stores category name', max_length=255)),
                ('category_type', models.CharField(help_text='Stores category type', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(help_text='stores product name', max_length=255)),
                ('product_type', models.CharField(help_text='stores product type', max_length=255)),
                ('image', models.URLField(default=None)),
                ('price of item', models.PositiveIntegerField()),
                ('product_desc', models.CharField(help_text='stores product name', max_length=255)),
                ('extra_data', models.TextField(help_text='Stores extra data about the product')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='forum.category')),
            ],
        ),
    ]