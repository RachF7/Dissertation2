# Generated by Django 2.1.5 on 2022-08-05 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diss', '0004_marker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discuss', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='anonymous', max_length=200)),
                ('email', models.CharField(max_length=200, null=True)),
                ('topic', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('link', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Marker',
        ),
        migrations.AddField(
            model_name='discussion',
            name='forum',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='diss.forum'),
        ),
    ]
