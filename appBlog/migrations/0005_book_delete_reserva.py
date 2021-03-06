# Generated by Django 4.0.4 on 2022-05-28 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0004_alter_curso_options_alter_estudiante_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('mail', models.EmailField(max_length=254)),
                ('event', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
    ]
