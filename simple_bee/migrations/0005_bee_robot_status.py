# Generated by Django 3.0.3 on 2020-02-16 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_bee', '0004_auto_20200215_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='bee_robot',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
