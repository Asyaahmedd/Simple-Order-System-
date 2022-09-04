from django.contrib import admin
from .models import Product,Purchase

class AdminPermissions(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True
    def has_change_permission(self, request,obj =None):
        return False
    def has_delete_permission(self, request,obj = None):
        return False
    def has_view_permission(self, request, obj = None) :
        return True

admin.site.register(Product)
admin.site.register(Purchase,AdminPermissions)