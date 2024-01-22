# Generated by Django 4.2.7 on 2024-01-22 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EkoloskaNavika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100)),
                ('opis', models.TextField()),
                ('kategorija', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Korisnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ekoloske_navike', models.ManyToManyField(to='main.ekoloskanavika')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocjena', models.IntegerField()),
                ('komentar', models.TextField()),
                ('navika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ekoloskanavika')),
            ],
        ),
        migrations.CreateModel(
            name='DnevnikEkoloskihAktivnosti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField()),
                ('opis', models.TextField()),
                ('navika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ekoloskanavika')),
            ],
        ),
    ]