# Generated by Django 3.1.4 on 2020-12-28 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20201227_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
