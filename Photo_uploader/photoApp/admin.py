from django.contrib import admin
from .models import uppic,cont
# Register your models here.

@admin.register(uppic)
class adminphoto(admin.ModelAdmin):
    list_display=['id','username','pic','desc','timedate']
    

@admin.register(cont)
class adminphoto(admin.ModelAdmin):
    list_display=['username','email','mob','message']