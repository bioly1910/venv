# Generated by Django 4.1.3 on 2022-12-23 13:11

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=embed_video.fields.EmbedVideoField(null=True),
        ),
    ]
