# Generated by Django 4.0.4 on 2022-05-29 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0005_book_delete_reserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('mail', models.EmailField(max_length=254)),
                ('age', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
    ]
