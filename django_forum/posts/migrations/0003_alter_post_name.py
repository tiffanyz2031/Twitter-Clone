# Generated by Django 4.0.3 on 2022-04-07 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_post_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, max_length=14, verbose_name='Name'),
        ),
    ]
