# Generated by Django 4.1.3 on 2022-11-24 11:53

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=mdeditor.fields.MDTextField(),
        ),
    ]