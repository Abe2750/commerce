# Generated by Django 4.0.1 on 2022-04-16 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('startBid', models.PositiveBigIntegerField()),
                ('image', models.URLField(null=True)),
                ('category', models.CharField(choices=[('Toys', 'Toys'), ('Elec', 'Electronics'), ('Fash', 'Fashion'), ('Home', 'Home')], default='Home', max_length=4, null=True)),
            ],
        ),
    ]
