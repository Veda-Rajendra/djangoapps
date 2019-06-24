from django.contrib import admin

from home.models import book,author,genre


# Register your models here.
#admin.site.register(book)
#admin.site.register(author)
#admin.site.register(genre)

@admin.register(book)
class bookAdmin(admin.ModelAdmin):
   # search_fields=('id','name')
    #list_filter=('book_name','date',('author_name,admin.RelatedOnlyFieldlistFilter'))
    #list_filter=('book_name','date','author_name')
    pass

@admin.register(author)
class authorAdmin(admin.ModelAdmin):
    pass

@admin.register(genre)
class genereAdmin(admin.ModelAdmin):
    pass