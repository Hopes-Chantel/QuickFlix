# Generated by Django 4.0.4 on 2022-05-02 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='genre',
            field=models.CharField(choices=[('Romantic Comedy', 'RC'), ('Thrillers', 'TR'), ('Drama', 'DR'), ('Comedy', 'CO'), ('Documentary', 'DO'), ('Family', 'FA')], default='Romantic Comedy', max_length=15),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='name',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Romantic Comedy', 'RC'), ('Thrillers', 'TR'), ('Drama', 'DR'), ('Comedy', 'CO'), ('Documentary', 'DO'), ('Family', 'FA')], default='Romantic Comedy', max_length=15),
        ),
    ]