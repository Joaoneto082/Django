# Generated by Django 3.2.12 on 2023-05-05 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0005_alter_contato_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(max_length=20),
        ),
    ]
