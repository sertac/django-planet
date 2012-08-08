# -*- coding: utf-8 -*-
"""
"""

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

SEARCH_CHOICES = (
    ("posts", _("Posts")),
    ("tags", _("Tags")),
    ("blogs", _("Blogs")),
    ("authors", _("Authors")),
    ("feeds", _("Feeds")),
)


class SearchForm(forms.Form):
    w = forms.ChoiceField(choices=SEARCH_CHOICES, label="")
    q = forms.CharField(max_length=100, label="")

import datetime
from planet.models import UserFeed

class DateFilterForm(forms.Form):
    feeds=forms.ChoiceField(required=False)
    start_date=forms.DateField()
    end_date=forms.DateField()

    def __init__(self,user, *args, **kwargs):
        super(DateFilterForm, self).__init__(*args, **kwargs)
        choices=UserFeed.objects.get(user=user).feeds.values_list('id','title')
        self.fields["feeds"].choices = choices
        self.fields['start_date'].input_formats = ['%m/%d/%Y']
        self.fields['end_date'].input_formats = ['%m/%d/%Y']