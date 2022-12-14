# Generated by Django 4.1.2 on 2022-10-20 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_category_menu_menuitem_delete_categorie_and_more'),
        ('books', '0006_alter_recipie_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipie',
            name='category',
            field=models.ManyToManyField(blank=True, to='core.category'),
        ),
        migrations.AddField(
            model_name='recipie',
            name='tags',
            field=models.ManyToManyField(blank=True, to='core.tag'),
        ),
        migrations.AlterField(
            model_name='recipie',
            name='images',
            field=models.ManyToManyField(blank=True, to='core.image'),
        ),
    ]
