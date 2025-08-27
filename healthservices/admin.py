from django.contrib import admin
from django.utils.html import format_html
from .models import Patient, AmbulanceDriver, AdminStaff

# Patient Admin
class PatientAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'location', 'is_accepted', 'is_finished', 'show_image')  # show_image is a method below

    def show_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%;" />', obj.image.url)
        return "-"
    show_image.short_description = 'Profile Image'


# AmbulanceDriver Admin
class AmbulanceDriverAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'location', 'is_active' , 'show_image')
    #change for aprovel
    list_filter = ('is_active',)
    search_fields = ('username', 'email')

    def show_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%;" />', obj.image.url)
        return "-"
    show_image.short_description = 'Profile Image'

    
# AdminStaff has no image, use default
class AdminStaffAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'show_image')

    def show_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%;" />', obj.image.url)
        return "-"
    show_image.short_description = 'Profile Image'
    
# Register all
admin.site.register(Patient, PatientAdmin)
admin.site.register(AmbulanceDriver, AmbulanceDriverAdmin)
admin.site.register(AdminStaff, AdminStaffAdmin)
