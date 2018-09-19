# Generated by Django 2.0.7 on 2018-07-26 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apprenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Formateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_hobby', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='formateur',
            name='hobbies',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_master.Hobbies'),
        ),
        migrations.AddField(
            model_name='apprenant',
            name='formateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_master.Formateur'),
        ),
        migrations.AddField(
            model_name='apprenant',
            name='hobbies',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_master.Hobbies'),
        ),
    ]