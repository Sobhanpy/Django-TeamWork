from django.contrib import admin
from .models import Post, Category, Tags, Comments, Replay

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','status', 'created_date']
    list_filter = ['status']
    search_fields = ['title']
    


admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Comments)
admin.site.register(Replay)