# Generated by Django 3.1.7 on 2021-03-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('discouted_price', models.IntegerField()),
                ('description', models.TextField()),
                ('brand', models.CharField(blank=True, max_length=200)),
                ('stock', models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=100)),
                ('labels', models.CharField(choices=[('new', 'new'), ('hot', 'hot'), ('sale', 'sale'), ('defult', 'default')], max_length=100)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
    ]
