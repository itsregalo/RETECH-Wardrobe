from django.contrib import admin
from .models import (Item, 
                     Manufacture, 
                     Upcoming_Product, 
                     Contact,
                     Category,
                     Order, OrderItem,
                     WishList, WishListItem,
                     Coupon
                    )


admin.site.site_header = "RETECH Mall"
admin.site.site_title = "RETECH Mall"

# Register your models here.
admin.site.register(Item)
admin.site.register(Manufacture)
admin.site.register(Upcoming_Product)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','subject']
    
admin.site.register(Contact, ContactAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    
admin.site.register(Category, CategoryAdmin)


admin.site.register(Order)
admin.site.register(OrderItem)

class WishListAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(WishList, WishListAdmin)

class WishListItemAdmin(admin.ModelAdmin):
    list_display = ['user','item']
    
admin.site.register(WishListItem, WishListItemAdmin)

admin.site.register(Coupon)