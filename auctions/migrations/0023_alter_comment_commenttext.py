# Generated by Django 4.0.1 on 2022-08-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_comment_commenter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentText',
            field=models.CharField(max_length=300),
        ),
    ]
