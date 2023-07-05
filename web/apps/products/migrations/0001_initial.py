# Generated by Django 4.2.1 on 2023-07-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand_seq', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(default='-', max_length=100)),
                ('brand_link', models.CharField(default='-', max_length=300)),
            ],
            options={
                'db_table': 'brands',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hash_seq', models.AutoField(primary_key=True, serialize=False)),
                ('hash_name', models.CharField(default='-', max_length=100)),
                ('hash_avg_price', models.IntegerField(default=0)),
                ('room_type', models.CharField(max_length=4)),
                ('hash_desc', models.CharField(default='-', max_length=1000)),
                ('hash_thumbnail', models.CharField(default='-', max_length=300)),
                ('is_active', models.CharField(default='Y', max_length=1)),
            ],
            options={
                'db_table': 'hashtags',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prod_seq', models.AutoField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(default='-', max_length=100)),
                ('prod_link', models.CharField(default='-', max_length=300)),
                ('prod_price', models.IntegerField(default=0)),
                ('prod_discount', models.IntegerField(default=0)),
                ('prod_thumbnail', models.CharField(default='-', max_length=300)),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductHashtag',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prod_hash_seq', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'productHashtags',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HashtagCategory',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hash_cate_seq', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(default='-', max_length=45)),
                ('room_type', models.CharField(default='-', max_length=4)),
                ('thumbnail', models.CharField(default='-', max_length=300)),
                ('description', models.CharField(default='-', max_length=100)),
            ],
            options={
                'db_table': 'hashtagCategories',
                'managed': True,
            },
        ),
    ]
