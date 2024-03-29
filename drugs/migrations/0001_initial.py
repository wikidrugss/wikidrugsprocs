# Generated by Django 2.2.3 on 2019-11-16 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('consulta', models.TextField(max_length=200)),
                ('respuesta', models.TextField(max_length=200)),
                ('respondida', models.BooleanField(default=False)),
            ],
        ),
    ]
