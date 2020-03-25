# Generated by Django 3.0.4 on 2020-03-24 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=105)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.RemoveField(
            model_name='brand',
            name='image',
        ),
    ]