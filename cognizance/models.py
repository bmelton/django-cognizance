from django.db import models
from django.utils.html import strip_tags, linebreaks
from django.contrib.sites.models import Site
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

# non-standard imports
from uuslug import uuslug

class Entry(models.Model):
    STATUSES = (
        ('Idea', _('idea')),
        ('Published', _('published')),
    )

    title           = models.CharField(max_length=100)
    slug            = models.CharField(max_length=100, null=True, blank=True)
    created         = models.DateTimeField(null=True, blank=True)
    modified        = models.DateTimeField(null=True, blank=True)
    start_date      = models.DateTimeField(null=True, blank=True)
    sites           = models.ToManyField(Site, related_name='Entries', verbose_name=_('sites')),
    content         = models.TextField(_('content'), blank=True)
    comments_on     = models.BooleanField(default=True)
    comment_count   = models.IntegerField(default=0)
    views           = models.IntegerField(default=0)
    excerpt         = models.CharField(max_length=250)
    active          = models.BooleanField(default=True)
    version         = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-created']
        verbose_name_plural = _('entries')
        

