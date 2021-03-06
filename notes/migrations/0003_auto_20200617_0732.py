# Generated by Django 3.0.6 on 2020-06-17 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_chemisrty'),
    ]

    operations = [
        migrations.CreateModel(
            name='botany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=50)),
                ('files', models.FileField(upload_to='uploads/')),
            ],
            options={
                'verbose_name_plural': 'Botany',
            },
        ),
        migrations.CreateModel(
            name='zoology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=50)),
                ('files', models.FileField(upload_to='uploads/')),
            ],
            options={
                'verbose_name_plural': 'Zoology',
            },
        ),
        migrations.DeleteModel(
            name='notes',
        ),
        migrations.AlterModelOptions(
            name='chemisrty',
            options={'verbose_name_plural': 'Chemistry'},
        ),
    ]
