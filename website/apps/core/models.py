from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

import watson


class SearchAdapter(watson.SearchAdapter):
    def get_title(self, obj):
        return obj.culture

    def get_content(self, obj):
        if obj.ethonyms:
            return 'Synonyms: ' + obj.ethonyms
        else:
            return ''


class TermSearchAdapter(watson.SearchAdapter):
    def get_title(self, obj):
        return obj.term

    def get_description(self, obj):
        return obj.definition

    def get_content(self, obj):
        return ''


class TrackedModel(models.Model):
    """Abstract base class containing editorial information"""
    editor = models.ForeignKey(User)
    added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
        get_latest_by = 'added'


class Glossary(TrackedModel):
    term = models.CharField(max_length=255, db_index=True)
    definition = models.TextField()

    def __unicode__(self):
        return self.term
    
    class Meta:
        verbose_name_plural = 'Glossary Terms'

    
class Source(TrackedModel):
    """Source Details"""
    year = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    author = models.CharField(
        max_length=255,
        db_index=True,
        help_text="Short Author list.  If the source has 2 authors, state this as "
                  "Smith & Johnson.  If the source has more than 2 authors, state Smith "
                  "et al.")
    slug = models.SlugField(
        max_length=1000,
        null=False,
        unique=True,
        help_text="`Slug` for author i.e. author-year (for use in URLS)")
    reference = models.TextField(
        blank=True, null=True, help_text="APA reference for Source.")
    bibtex = models.TextField(
        blank=True, null=True, help_text="BibTeX entry")
    comment = models.TextField(
        blank=True, null=True, help_text="Private comment on source")
    
    def __unicode__(self):
        if self.year is not None:
            return mark_safe("%s (%s)" % (self.author, self.year))
        return self.author

    @models.permalink
    def get_absolute_url(self):
        return ('source-detail', [self.slug])
    
    class Meta:
        db_table = 'sources'
        ordering = ['author', 'year', ]
        index_together = [
            ["author", "year"],
        ]
        unique_together = ['author', 'year']


class Language(TrackedModel):
    isocode = models.CharField(max_length=3, db_index=True, help_text="ISO-639-3 Code")
    language = models.CharField(max_length=255, db_index=True, help_text="Language Name")

    classification = models.TextField(help_text="Classification String")
    abvdcode = models.IntegerField(db_index=True, unique=True, null=True, blank=True)
    
    def __unicode__(self):
        return self.language

    class Meta:
        unique_together = ("isocode", "language")
        db_table = 'languages'
        ordering = ['language']


class Category(TrackedModel):
    category = models.CharField(max_length=128)
    number = models.IntegerField(
        blank=True,
        null=True,
        help_text="Category number - for order displayed on website")
    timeFocus = models.BooleanField(
        "No time focus associated with this category", default=False)

    def __unicode__(self):
        return self.category
    
    class Meta:
        db_table = 'categories'
        ordering = ['category']
        verbose_name_plural = 'Broad Categories'


class Section(TrackedModel):
    category = models.ForeignKey(
        Category, blank=True, null=True, help_text="Category that this Section belongs to"
    )
    
    section = models.CharField(max_length=128)
    
    slug = models.SlugField(
        max_length=128, unique=True, help_text="`Slug` for this section (for use in URLS)"
    )
    notes = models.TextField(
        blank=True, null=True, help_text="Public Notes on this section")
    
    number = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return self.section

    class Meta:
        db_table = 'sections'
        ordering = ['id']
        
            
class Culture(TrackedModel):
    culture = models.CharField(
        max_length=128, db_index=True, unique=True, help_text="Name of culture")
    slug = models.SlugField(
        max_length=128, help_text="`Slug` for this section (for use in URLS)")
    notes = models.TextField(
        blank=True, null=True, help_text="Brief description of culture (2-3 sentences)")
    
    # need to change this name to ethnoyms!
    ethonyms = models.TextField(
        "Ethonyms",
        blank=True,
        null=True,
        help_text="Ethonyms for this culture. Please separate ethonyms with a semicolon "
                  "and space, e.g. 'Ethonym 1; Ethonym 2, East' (without the quotation "
                  "marks). Do not enter the culture's name as an ethonym. Do not use a "
                  "semicolon within an ethonym.")

    languages = models.ManyToManyField(
        Language, help_text="The languages affiliated with this culture.")
    
    coder = models.CharField(
        max_length=256, blank=True, null=True, help_text="Coder's full name")

    def __unicode__(self):
        return self.culture
    
    @models.permalink
    def get_absolute_url(self):
        return ('culture-detail', [self.slug])

    class Meta:
        db_table = 'cultures'
        ordering = ['culture']


class Publication(TrackedModel):
    link = models.CharField(
        max_length=128,
        unique=True,
        blank=True,
        null=True,
        help_text="Link to this publication. Must be a complete link (not just a doi). "
                  "Leave blank if no link to article.")
    reference = models.TextField(help_text="Full APA reference for this publication.")

    def __unicode__(self):
        return self.reference
    
watson.register(Glossary, TermSearchAdapter)
watson.register(
    Culture,
    SearchAdapter,
    fields=(
        "culture",
        "ethonyms",
        "languages__isocode",
        "languages",
        "languages__abvdcode",
        "coder",),
    exclude=("notes",))
