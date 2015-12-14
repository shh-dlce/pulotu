# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=128)),
                ('number', models.IntegerField(help_text=b'Category number - for order displayed on website', null=True, blank=True)),
                ('timeFocus', models.BooleanField(default=False, verbose_name=b'No time focus associated with this category')),
                ('editor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['category'],
                'db_table': 'categories',
                'verbose_name_plural': 'Broad Categories',
            },
        ),
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('culture', models.CharField(help_text=b'Name of culture', unique=True, max_length=128, db_index=True)),
                ('slug', models.SlugField(help_text=b'`Slug` for this section (for use in URLS)', max_length=128)),
                ('notes', models.TextField(help_text=b'Brief description of culture (2-3 sentences)', null=True, blank=True)),
                ('ethonyms', models.TextField(help_text=b"Ethonyms for this culture. Please separate ethonyms with a semicolon and space, e.g. 'Ethonym 1; Ethonym 2, East' (without the quotation marks). Do not enter the culture's name as an ethonym. Do not use a semicolon within an ethonym.", null=True, verbose_name=b'Ethonyms', blank=True)),
                ('coder', models.CharField(help_text=b"Coder's full name", max_length=256, null=True, blank=True)),
                ('editor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['culture'],
                'db_table': 'cultures',
            },
        ),
        migrations.CreateModel(
            name='Glossary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('term', models.CharField(max_length=255, db_index=True)),
                ('definition', models.TextField()),
                ('editor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Glossary Terms',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('isocode', models.CharField(help_text=b'ISO-639-3 Code', max_length=3, db_index=True)),
                ('language', models.CharField(help_text=b'Language Name', max_length=255, db_index=True)),
                ('classification', models.TextField(help_text=b'Classification String')),
                ('abvdcode', models.IntegerField(db_index=True, unique=True, null=True, blank=True)),
                ('editor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['language'],
                'db_table': 'languages',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('link', models.CharField(help_text=b'Link to this publication. Must be a complete link (not just a doi). Leave blank if no link to article.', max_length=128, unique=True, null=True, blank=True)),
                ('reference', models.TextField(help_text=b'Full APA reference for this publication.')),
                ('editor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'get_latest_by': 'added',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('section', models.CharField(max_length=128)),
                ('slug', models.SlugField(help_text=b'`Slug` for this section (for use in URLS)', unique=True, max_length=128)),
                ('notes', models.TextField(help_text=b'Public Notes on this section', null=True, blank=True)),
                ('number', models.IntegerField(null=True, blank=True)),
                ('category', models.ForeignKey(blank=True, to='core.Category', help_text=b'Category that this Section belongs to', null=True)),
                ('editor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'sections',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('year', models.CharField(db_index=True, max_length=255, null=True, blank=True)),
                ('author', models.CharField(help_text=b'Short Author list.  If the source has 2 authors, state this as Smith & Johnson.  If the source has more than 2 authors, state Smith et al.', max_length=255, db_index=True)),
                ('slug', models.SlugField(help_text=b'`Slug` for author i.e. author-year (for use in URLS)', unique=True, max_length=1000)),
                ('reference', models.TextField(help_text=b'APA reference for Source.', null=True, blank=True)),
                ('bibtex', models.TextField(help_text=b'BibTeX entry', null=True, blank=True)),
                ('comment', models.TextField(help_text=b'Private comment on source', null=True, blank=True)),
                ('editor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['author', 'year'],
                'db_table': 'sources',
            },
        ),
        migrations.AddField(
            model_name='culture',
            name='languages',
            field=models.ManyToManyField(help_text=b'The languages affiliated with this culture.', to='core.Language'),
        ),
        migrations.AlterUniqueTogether(
            name='source',
            unique_together=set([('author', 'year')]),
        ),
        migrations.AlterIndexTogether(
            name='source',
            index_together=set([('author', 'year')]),
        ),
        migrations.AlterUniqueTogether(
            name='language',
            unique_together=set([('isocode', 'language')]),
        ),
    ]
