# Generated by Django 4.1.5 on 2023-02-21 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0003_building_residential_alter_building_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='color',
            field=models.CharField(default='Brick Red', max_length=50),
        ),
    ]
