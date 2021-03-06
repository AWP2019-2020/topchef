# Generated by Django 2.2.7 on 2020-01-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0002_category_comment_recipe_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='selfdescription',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
