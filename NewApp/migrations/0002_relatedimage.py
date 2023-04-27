# Generated by Django 4.1.6 on 2023-03-07 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NewApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='relatedimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(null=True, upload_to='Relatedimages')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewApp.product')),
            ],
        ),
    ]
