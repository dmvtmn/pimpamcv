from django.contrib import admin
from .models import Category, UsrDoc, Service, ServiceImage

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'price','updated','active']
    list_editable = ['price', 'active'] #so that we can change price and active status
    readonly_fields = ['updated', 'timestamp']
    prepopulated_fields = {"slug":("title",)}

    class Meta:
        model = Service
admin.site.register(Service,ServiceAdmin)

class UsrDocAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['title']
    list_display = ['__unicode__', 'user','title','updated']
    list_filter = ['user', 'active']
    readonly_fields = ['updated', 'timestamp']

    class Meta:
        model = UsrDoc
admin.site.register(UsrDoc,UsrDocAdmin)


admin.site.register(Category)
admin.site.register(ServiceImage)
