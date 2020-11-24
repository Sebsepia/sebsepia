from django.contrib import admin
from .models import Post, BlogImage, FreeImage



class FImageInline(admin.TabularInline):
    model = FreeImage
    extra = 0

class BImageInline(admin.TabularInline):
    model = BlogImage
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date' )
    fields = [('title', 'title_tag', 'slug'),('talkshit'),('text_color','bg_color', 'bg_color_a' ),('bg_overlay_color', 'bg_overlay_check' ),('tags','post_date')]
    inlines = [FImageInline, BImageInline]
admin.site.register(Post, PostAdmin)

class BImageAdmin(admin.ModelAdmin):
    list_display = ('b_img', 'b_img_date')
    fields = [('b_img', 'b_img_date')]
admin.site.register(BlogImage, BImageAdmin)
