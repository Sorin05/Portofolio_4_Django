from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Routine, Comment



@admin.register(Routine)
class RoutineAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('routine_name',)}
    list_filter = ('status', 'added_on', 'updated_on', 'likes')
    list_display = ('routine_name', 'added_on', 'status', 'updated_on')
    search_fields = ('routine_name', 'description', 'method')
    summernote_fields = ('description', 'method')
    actions = ['approve_routine']

    def approve_routine(self, request, queryset):
        queryset.update(status=1)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'routine', 'added_on', 'approved')
    list_filter = ('approved', 'added_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
