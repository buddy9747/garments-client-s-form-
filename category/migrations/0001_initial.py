# Generated by Django 2.0 on 2018-07-19 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabric', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Garment', 'Garment'), ('Hardgoods', 'Hardgoods'), ('Home Furnishing', 'Home Furnishing')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('dept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Department')),
                ('fab', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Fabric')),
                ('fact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Factory')),
            ],
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsection', models.CharField(blank=True, max_length=500, null=True, unique=True)),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Sections')),
            ],
        ),
        migrations.CreateModel(
            name='Wash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wash', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Fabric')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='sect',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Sections'),
        ),
        migrations.AddField(
            model_name='person',
            name='subcat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Subcategory'),
        ),
        migrations.AddField(
            model_name='person',
            name='subsect',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Subsection'),
        ),
        migrations.AddField(
            model_name='person',
            name='was',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Wash'),
        ),
        migrations.AddField(
            model_name='fabric',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Factory'),
        ),
        migrations.AddField(
            model_name='department',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Subcategory'),
        ),
        migrations.AddField(
            model_name='category',
            name='cat',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='category.Factory'),
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Wash'),
        ),
    ]