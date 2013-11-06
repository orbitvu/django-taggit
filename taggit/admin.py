from __future__ import unicode_literals

from django.contrib import admin

from taggit.models import Tag, TaggedItem


class TaggedItemInline(admin.StackedInline):
    model = TaggedItem

class TagAdmin(admin.ModelAdmin):
    inlines = [
        TaggedItemInline
    ]
    list_display = ["user", "name", "slug"]
    ordering = ["user", "name", "slug"]
    search_fields = ["user", "name"]
    prepopulated_fields = {"slug": ["name"]}


admin.site.register(Tag, TagAdmin)
