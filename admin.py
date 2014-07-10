# -*- coding: utf8 -*-
from django.contrib import admin

from eventsplanning.models import Event, HackerBatch


class EventAdmin(admin.ModelAdmin):

    list_display = ('titre', 'description', 'published', 'interne', 'programme')
    list_filter = ('published', 'interne', 'responsable')
    list_editable = ('published', 'interne')
    ordering = ['titre']

    # TODO
    #fieldsets = (
        #(None,      {'fields': ['theme', 'responsable', 'description']}),
        #('Date',    {'fields': ['date']}),
        #('Visibilité', {'fields': ['published', 'interne', 'programme']})
    #)




admin.site.register(Event, EventAdmin)
