from django.contrib import admin
from .models import Product, Category, Store
from .forms import ProductAdminForm

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
     
    list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)

    prepopulated_fields = {'slug' : ('name',)}
    
admin.site.register(Product, ProductAdmin)
    
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    
    prepopulated_fields = {'slug' : ('name',)}
    
admin.site.register(Category, CategoryAdmin)

class StoreAdmin(admin.ModelAdmin):
    
    def activate(self, request, queryset):
        rows_updated = queryset.update(active=True)
        
        if rows_updated == 1:
            message_bit = "1 store was"
        else:
            message_bit = "%s store were" % rows_updated
        self.message_user(request, "%s successfully activated." % message_bit)
    
    activate.short_description = "Activate Stores"

    actions = [activate]
    list_display = ['id','name','code','currency_rate','tax_rate','agent_share','created', 'active'] 

admin.site.register(Store, StoreAdmin)