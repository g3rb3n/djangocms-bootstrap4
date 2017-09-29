# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.utils.translation import ugettext_lazy as _
from django.conf import settings


DEVICE_CHOICES = (
    ('xs', _('Extra small')),   # default <576px
    ('sm', _('Small')),         # default ≥576px
    ('md', _('Medium')),        # default ≥768px
    ('lg', _('Large')),         # default ≥992px
    ('xl', _('Extra large')),   # default ≥1200px
)
DEVICE_SIZES = tuple([size for size, name in DEVICE_CHOICES])

TAG_CHOICES = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_TAG_CHOICES',
    ['div', 'section', 'article', 'header', 'footer', 'aside'],
)
TAG_CHOICES = tuple((entry, entry) for entry in TAG_CHOICES)