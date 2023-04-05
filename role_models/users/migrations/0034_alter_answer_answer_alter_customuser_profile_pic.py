# Generated by Django 4.0.2 on 2023-04-03 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_alter_customuser_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
