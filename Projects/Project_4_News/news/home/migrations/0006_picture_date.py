# Generated by Django 3.1.7 on 2021-04-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210410_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]