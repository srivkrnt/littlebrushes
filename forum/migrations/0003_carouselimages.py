# Generated by Django 4.0.6 on 2022-07-17 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_rename_price of item_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
    ]
