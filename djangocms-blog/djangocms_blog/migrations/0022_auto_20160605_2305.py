# Generated by Django 1.9.7 on 2016-06-05 21:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("djangocms_blog", "0021_post_liveblog"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="enable_liveblog",
            field=models.BooleanField(default=False, verbose_name="enable liveblog on post"),
        ),
    ]
