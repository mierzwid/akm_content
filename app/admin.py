from django.contrib import admin
from django.contrib.flatpages.models import FlatPage

# Override flatpage admin
class FlatPageAdmin(admin.ModelAdmin):
    class Media:
        js = ('/media/js/jquery.js', 
              '/media/js/admin_enhancements.js',
              '/media/js/ckeditor/ckeditor.js')
        css = {'screen': ('/media/c/admin.css',)}
    
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

