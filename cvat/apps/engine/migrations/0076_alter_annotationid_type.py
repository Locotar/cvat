# Generated by Django 3.2.18 on 2023-04-30 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0075_alter_annotationconflict_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotationid',
            name='type',
            field=models.CharField(choices=[('tag', 'TAG'), ('track', 'TRACK'), ('rectangle', 'RECTANGLE'), ('polygon', 'POLYGON'), ('polyline', 'POLYLINE'), ('points', 'POINTS'), ('ellipse', 'ELLIPSE'), ('cuboid', 'CUBOID'), ('mask', 'MASK'), ('skeleton', 'SKELETON')], max_length=32),
        ),
    ]
