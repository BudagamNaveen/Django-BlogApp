from django.contrib import admin
from .models import BlogData,CommentSection,NewBlogData

# Register your models here.
admin.site.register(BlogData)
admin.site.register(CommentSection)
admin.site.register(NewBlogData)