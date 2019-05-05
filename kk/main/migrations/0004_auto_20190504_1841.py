# Generated by Django 2.2.1 on 2019-05-04 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190504_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='Body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='topic',
            name='Category',
            field=models.CharField(choices=[('phy', 'Physics'), ('che', 'Chemistry'), ('bio', 'Biology'), ('eng', 'English'), ('ara', 'Arabic'), ('his', 'History'), ('art', 'Arts'), ('ict', 'Computer science'), ('mth', 'Maths'), ('gen', 'General')], default='gen', max_length=3),
        ),
        migrations.AlterField(
            model_name='topic',
            name='Title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='Age',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='Phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='Region',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='Type',
            field=models.CharField(choices=[('DEF', 'Student'), ('PRV', 'Instructor/Moderator')], default='DEF', max_length=3),
        ),
    ]
