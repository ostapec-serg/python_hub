from django.contrib import admin

from scrap.models import Ask, Job, Show, New, StoryCategory


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'by', 'id_story')
    list_display_links = ('by', 'title', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    list_display_links = ('category', )


admin.site.register(Ask, StoryAdmin)
admin.site.register(Job, StoryAdmin)
admin.site.register(New, StoryAdmin)
admin.site.register(Show, StoryAdmin)
admin.site.register(StoryCategory, CategoryAdmin)
