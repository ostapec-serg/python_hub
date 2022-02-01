from django.contrib import admin

from scrap.models import Ask, Job, Show, New


class StoryAdmin(admin.ModelAdmin):
    list_display = ('id_story', 'by', 'title', )
    list_display_links = ('id_story', 'title', )


admin.site.register(Ask, StoryAdmin)
admin.site.register(Job, StoryAdmin)
admin.site.register(New, StoryAdmin)
admin.site.register(Show, StoryAdmin)
