# Generated by Django 3.1.1 on 2020-09-10 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_mangainfo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mangainfo',
            name='manga_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mangatype', to='home.mangatype'),
        ),
    ]
