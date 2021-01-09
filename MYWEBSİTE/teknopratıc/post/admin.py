from django.contrib import admin
from post.models import Post

from post.models import Quote

from post.models import Infoabouttek



class infotek(admin.ModelAdmin):
    pass






class soz(admin.ModelAdmin):
    
    pass





class Postadmin(admin.ModelAdmin):
    list_display=["title","publishing_date"]
    list_display_links=["title","publishing_date"]
    list_filter=["publishing_date"]
    search_fields=["title"]
    prepopulated_fields={"slug":("title",)}

    
   
    


    class Meta:
        model=Post
        




admin.site.register(Post,Postadmin)


admin.site.register(Quote,soz)


admin.site.register(Infoabouttek,infotek)







