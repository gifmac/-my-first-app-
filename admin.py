# Register your models here.
from django.contrib import admin
from .models import Post, Publisher  # .model means to import from the same package

# to make our model visible to the admin page we need to register  the model with admin.site.register
# admin.site.register(Post, PostAdmin)

# note that the class Publisher  was not showing in the admin, we have to import them
# using import  Publisher, and use register to register it

class PublisherInLine(admin.TabularInline):
    model = Publisher
    extra = 3

class PostAdmin(admin.ModelAdmin):
    fieldsets = [(None,   {"fields": ["pub_date"]}), ("Date information",

                         {"fields": ["title"], "classes": ["collapse"]}), ]
    inlines = [PublisherInLine]


admin.site.register(Post, PostAdmin)






