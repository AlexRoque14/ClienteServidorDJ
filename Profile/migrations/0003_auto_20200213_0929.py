# Generated by Django 2.2.1 on 2020-02-13 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_modelestado'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelCiudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ModelEstadoCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estadoCivil', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ModelGenero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ModelOcupacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupacion', models.CharField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='modelestado',
            name='estado',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ciudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.ModelCiudad'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.ModelEstado'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='estadoCivil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.ModelEstadoCivil'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.ModelGenero'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ocupacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.ModelOcupacion'),
        ),
    ]
