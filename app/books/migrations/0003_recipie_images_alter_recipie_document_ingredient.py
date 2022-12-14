# Generated by Django 4.1.2 on 2022-10-16 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_categorie_contributor_image_metadata_tag_and_more'),
        ('books', '0002_recipie_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipie',
            name='images',
            field=models.ManyToManyField(to='core.image'),
        ),
        migrations.AlterField(
            model_name='recipie',
            name='document',
            field=models.JSONField(default=dict),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=175)),
                ('in_recipie', models.ManyToManyField(to='books.recipie')),
            ],
        ),
    ]
