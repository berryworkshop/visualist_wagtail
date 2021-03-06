from django import forms
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.timezone import now

from wagtail.api import APIField
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel, FieldRowPanel)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from taggit.models import TaggedItemBase

from visualist.models import Record
from names.models import Agent


class Event(Record):
    schema = 'http://schema.org/Event'

    # see: https://goo.gl/vA8HD8
    start_date = models.DateTimeField(default=now)
    duration = models.PositiveIntegerField(default=0)
    precision = models.PositiveIntegerField(default=0)
    categories = ParentalManyToManyField('EventCategory', blank=True)
    tags = ClusterTaggableManager(through='EventTag', blank=True)
    organizers = ParentalManyToManyField(Agent, blank=True,
        related_name='organizer_of')

    venues = ParentalManyToManyField('names.Organization', blank=True)
    locations = ParentalManyToManyField('places.Place', blank=True)


    # TODO: more ParentalManyToManyFields for these?
    # contributors
    # curators
    # exhibitors
    # performers

    # venues = ParentalManyToManyField(Agent,
        # blank=True) # TODO: link to Organization, or Place?

    STATUSES = (
        ('cancelled', 'cancelled'),
    )
    event_status = models.CharField(
        choices=STATUSES,
        blank=True,
        null=True,
        max_length=25)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    def endDate(self): # TODO
        return self.startDate

    def citation(self): # TODO
        pass

    def date(self): # TODO
        pass

    search_fields = Record.search_fields + []
    parent_page_types = ['events.EventIndex', 'events.Event']
    content_panels = Record.content_panels + [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('start_date'),
                FieldPanel('duration'),
                FieldPanel('precision')
            ]),
            FieldPanel('event_status'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            FieldPanel('tags'),
        ], heading="Event information"),
        InlinePanel('gallery_images', label="Gallery images"),
        FieldPanel('organizers', widget=forms.CheckboxSelectMultiple),
    ]
    api_fields = [
        APIField('published_date'),
        APIField('gallery_images'),
    ]

    class Meta:
        unique_together = (
            ("start_date", "duration", 'precision'),)

class EventTag(TaggedItemBase):
    content_object = ParentalKey('Event', related_name='tagged_items')


class EventIndex(Page):
    schema = 'http://schema.org/ItemList'

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        events = self.get_children().live().order_by('-first_published_at')
        context['events'] = events
        return context


class EventGalleryImage(Orderable):

    event = ParentalKey(Event, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class EventTagIndex(Page):
    schema = 'http://schema.org/ItemList'

    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        events = Event.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['events'] = events
        return context


@register_snippet
class EventCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'event categories'
