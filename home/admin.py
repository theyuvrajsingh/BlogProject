from django.contrib import admin
from .models import *

# For configuration of Category Admin by me......
class categoryAdmin(admin.ModelAdmin):
    list_display=('image_tag','title','description','add_date')
    search_fields=('title',)
 

# For configuation of Post model in admin by me .....




admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(category,categoryAdmin)
