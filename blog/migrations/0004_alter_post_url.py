# Generated by Django 4.1.3 on 2022-12-23 15:34

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]
