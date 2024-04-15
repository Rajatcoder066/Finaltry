# Generated by Django 3.1.14 on 2023-04-22 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_registration_email_alter_registration_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=10000)),
                ('price', models.CharField(max_length=1000)),
                ('offer', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('spec', models.CharField(max_length=1000)),
                ('category', models.CharField(max_length=1000)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]