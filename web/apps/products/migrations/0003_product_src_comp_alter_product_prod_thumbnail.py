# Generated by Django 4.2.1 on 2023-06-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_hashtag_alter_product_prod_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='src_comp',
            field=models.CharField(default='-', max_length=45),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_thumbnail',
            field=models.CharField(default='-', max_length=300),
        ),
    ]