from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display=['Name','Email','Dob','State','Gender','Location',
                'Profile_pic','File_upload']

admin.site.register(Profile,ProfileAdmin)




