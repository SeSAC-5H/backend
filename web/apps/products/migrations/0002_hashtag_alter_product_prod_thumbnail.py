# Generated by Django 4.1.7 on 2023-06-05 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hash_seq', models.AutoField(primary_key=True, serialize=False)),
                ('hash_name', models.CharField(default='-', max_length=100)),
                ('room_type', models.CharField(default='-', max_length=4)),
                ('hash_desc', models.CharField(default='-', max_length=1000)),
            ],
            options={
                'db_table': 'hashtags',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_thumbnail',
            field=models.IntegerField(default=0),
        ),
    ]