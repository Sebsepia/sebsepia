from django.contrib import admin
from .models import Post, BlogImage, PanoImage, PortfolioCategory, SketchbookCategory

from django.forms import TextInput, Textarea
from django.db import models

class BImageInline(admin.TabularInline):
    model = BlogImage
    exclude = ('b_img_resize',)
    extra = 1
    formfield_overrides = {
        #models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
    }
class PImageInline(admin.TabularInline):
    model = PanoImage
    extra = 1
    formfield_overrides = {
        #models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }


class PostInline(admin.TabularInline):
    model = Post
    exclude = ('title_tag','slug','tags')
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date', 'tags' )
    fields = [('title', 'title_tag', 'slug'),('tags','post_date'),('portfolio_category', 'sketchbook_category')]
    inlines = [ BImageInline, PImageInline]
admin.site.register(Post, PostAdmin)

class PortfolioCatAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    fields = [('category_name', )]

admin.site.register(PortfolioCategory, PortfolioCatAdmin)

class SketchbookCatAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    fields = [('category_name', 'cover_img' )]
    inlines = [PostInline]
admin.site.register(SketchbookCategory, SketchbookCatAdmin)

class BlogImageAdmin(admin.ModelAdmin):
    list_display = ('b_img', 'b_img_resize')
    fields = [('b_img', 'b_img_resize')]
admin.site.register(BlogImage, BlogImageAdmin)
