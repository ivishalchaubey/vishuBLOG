from django.contrib import admin

from blog.models import blogPostModel,useremail

class blogPostAdmin(admin.ModelAdmin):
    list_display = ("blog_title","blog_time","blog_image","blog_slug")
    
admin.site.register(blogPostModel,blogPostAdmin)
admin.site.register(useremail)