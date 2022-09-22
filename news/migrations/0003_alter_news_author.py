# Generated by Django 3.2 on 2022-09-22 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('news', '0002_alter_news_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.author'),
        ),
    ]
