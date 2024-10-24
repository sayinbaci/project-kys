from django.contrib import admin
from .models import Post #from post.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
   
   list_display = ['title', 'publishing_date','content','slug']
   list_display_links = ['title', 'publishing_date']
   list_filter = ['publishing_date']
   search_fields = ['title', 'content']
   list_editable = ['content']
   

   class Meta:
     model = Post

admin.site.register(Post, PostAdmin)

