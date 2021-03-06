# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 06:51
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actuation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Instituition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('cpf', models.CharField(help_text='Ex.: 111.111.111-11 ou 11111111111', max_length=14, validators=[django.core.validators.MinLengthValidator(11)], verbose_name='CPF')),
                ('rg', models.CharField(max_length=20, verbose_name='RG')),
                ('contact', models.CharField(max_length=11, verbose_name='Contato')),
                ('student_ifpi', models.BooleanField(default=False, verbose_name='Aluno do IFPI')),
                ('matriculation', models.CharField(blank=True, help_text='Se não for aluno do IFPI, deixe em branco.', max_length=12, null=True, verbose_name='Matrícula')),
                ('scholarship_holder', models.BooleanField(default=False, verbose_name='Bolsista')),
                ('active', models.BooleanField(default=False, verbose_name='Ativo')),
                ('entry_date', models.DateField(verbose_name='Data de Entrada')),
                ('departure_date', models.DateField(blank=True, null=True, verbose_name='Data de Saída')),
                ('actuations', models.ForeignKey(help_text='Mantenha pressionado o Control (CTRL), ou Command no Mac, para selecionar mais de uma opção.', on_delete=django.db.models.deletion.CASCADE, to='members.Actuation', verbose_name='Atuações')),
                ('instituition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Instituition', verbose_name='Instituição')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Position', verbose_name='Cargo'),
        ),
        migrations.AddField(
            model_name='member',
            name='specialties',
            field=models.ForeignKey(help_text='Mantenha pressionado o Control (CTRL), ou Command no Mac, para selecionar mais de uma opção.', on_delete=django.db.models.deletion.CASCADE, to='members.Specialty', verbose_name='Especialidades'),
        ),
    ]
