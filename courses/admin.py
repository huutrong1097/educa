from django.contrib import admin
from .models import Subject, Course, Module
# Register your models here.
admin.site.index_template = 'memcache_status/admin_index.html'
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    prepopulated_fields = {'slug': ('title',)}

class ModuleInline(admin.StackedInline):#
    # This is used for editing models on the same page as a parent model. These are called inlines.
    # There are 2 format: TabularInline and StackedInline
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # The attribute prepopulated_fields tells the admin application to automatically fill the field slug
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
