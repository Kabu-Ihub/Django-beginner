from django.contrib import admin
from .models import Posts

class PostModelAdmin(admin.ModelAdmin):
  list_display =["title","Updated","published"]
  list_filter =["published","Updated"]
  list_display_links =["Updated"]
  list_editable =["title"]
  search_fields =["title","content"]
  class Meta:
    model = Posts

admin.site.register(Posts,PostModelAdmin)