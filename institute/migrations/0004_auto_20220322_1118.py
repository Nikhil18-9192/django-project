# Generated by Django 3.1.3 on 2022-03-22 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0003_alter_student_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
