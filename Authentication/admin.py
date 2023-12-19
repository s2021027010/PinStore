from django.contrib import admin

from .models import db_Profile, db_Profile_detail

# Register your models here.
 
class Product_Inline(admin.TabularInline):
    model =  db_Profile_detail

class db_Product_Inline(admin.ModelAdmin):
    inlines = [Product_Inline]

admin.site.register(db_Profile, db_Product_Inline)