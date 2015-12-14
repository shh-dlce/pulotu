# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import polymorphic.showfields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('publicNumber', models.IntegerField(help_text=b'For public order of questions', null=True, verbose_name=b'Public Number', blank=True)),
                ('number', models.IntegerField(help_text=b'The sequence number for this question', db_index=True)),
                ('question', models.CharField(help_text=b'The Question. Anything you do not want visible to the general public should go in the Information section.', unique=True, max_length=255, db_index=True)),
                ('simplified_question', models.CharField(max_length=255, null=True, blank=True)),
                ('information', models.TextField(help_text=b'Information to display to the coder', blank=True)),
                ('response_type', models.CharField(default=b'Int', help_text=b'The expected response type', max_length=6, choices=[(b'Int', b'Integer'), (b'Float', b'Float'), (b'Text', b'Text'), (b'Option', b'Options')])),
                ('displayPublic', models.BooleanField(default=False, verbose_name=b'Hide this question from the public')),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('codersnotes', models.TextField(help_text=b'Notes from the Coder on these responses', null=True, verbose_name=b"Coder's Notes", blank=True)),
                ('uncertainty', models.BooleanField(default=False)),
                ('missing', models.BooleanField(default=False, verbose_name=b'Missing data')),
                ('page1', models.CharField(max_length=256, null=True, blank=True)),
                ('page2', models.CharField(max_length=256, null=True, blank=True)),
                ('page3', models.CharField(max_length=256, null=True, blank=True)),
                ('page4', models.CharField(max_length=256, null=True, blank=True)),
                ('page5', models.CharField(max_length=256, null=True, blank=True)),
            ],
            options={
                'db_table': 'responses',
            },
            bases=(polymorphic.showfields.ShowFieldType, models.Model),
        ),
        migrations.CreateModel(
            name='FloatResponse',
            fields=[
                ('response_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='survey.Response')),
                ('response', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'responses_floats',
            },
            bases=('survey.response',),
        ),
        migrations.CreateModel(
            name='IntegerResponse',
            fields=[
                ('response_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='survey.Response')),
                ('response', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'responses_integers',
            },
            bases=('survey.response',),
        ),
        migrations.CreateModel(
            name='OptionQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='survey.Question')),
                ('options', models.TextField(help_text=b'The possible options. MUST be in the following format, with ONE option per line:\n\n    (?) Missing data\n    (0) Low\n    (1) Moderate\n    (2) High\n    ')),
            ],
            options={
                'db_table': 'questions_option',
            },
            bases=('survey.question',),
        ),
        migrations.CreateModel(
            name='OptionResponse',
            fields=[
                ('response_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='survey.Response')),
                ('response', models.CharField(max_length=3, null=True, blank=True)),
                ('response_text', models.TextField(help_text=b'The text response from the user. We save this only for debugging purposes.', null=True, blank=True)),
            ],
            options={
                'db_table': 'responses_options',
            },
            bases=('survey.response',),
        ),
        migrations.CreateModel(
            name='TextResponse',
            fields=[
                ('response_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='survey.Response')),
                ('response', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'responses_texts',
            },
            bases=('survey.response',),
        ),
        migrations.AddField(
            model_name='response',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='response',
            name='culture',
            field=models.ForeignKey(to='core.Culture'),
        ),
        migrations.AddField(
            model_name='response',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_survey.response_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='response',
            name='question',
            field=models.ForeignKey(to='survey.Question'),
        ),
        migrations.AddField(
            model_name='response',
            name='source1',
            field=models.ForeignKey(related_name='source1', blank=True, to='core.Source', null=True),
        ),
        migrations.AddField(
            model_name='response',
            name='source2',
            field=models.ForeignKey(related_name='source2', blank=True, to='core.Source', null=True),
        ),
        migrations.AddField(
            model_name='response',
            name='source3',
            field=models.ForeignKey(related_name='source3', blank=True, to='core.Source', null=True),
        ),
        migrations.AddField(
            model_name='response',
            name='source4',
            field=models.ForeignKey(related_name='source4', blank=True, to='core.Source', null=True),
        ),
        migrations.AddField(
            model_name='response',
            name='source5',
            field=models.ForeignKey(related_name='source5', blank=True, to='core.Source', null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='editor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_survey.question_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='section',
            field=models.ForeignKey(verbose_name=b'Subsection', to='core.Section', help_text=b'The specific section this question belongs to'),
        ),
        migrations.AddField(
            model_name='question',
            name='subsection',
            field=models.ForeignKey(related_name='Section', verbose_name=b'Section', to='core.Section', help_text=b'The broad section this question belongs to'),
        ),
        migrations.AlterUniqueTogether(
            name='response',
            unique_together=set([('question', 'culture')]),
        ),
    ]
