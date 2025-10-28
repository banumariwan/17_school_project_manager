from django.contrib import admin
from .models import Student, ClassRoom

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'classroom', 'joined_date')
    search_fields = ('name', 'email')
    list_filter = ('classroom',)

admin.site.register(Student, StudentAdmin)
admin.site.register(ClassRoom)
