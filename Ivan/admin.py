from django.contrib import admin
from .models import Project, Skill, About

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'order']
    list_filter = ['date_created', 'technologies']
    search_fields = ['title', 'description']
    ordering = ['-order', '-date_created']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description')
        }),
        ('Links', {
            'fields': ('link', 'github_link')
        }),
        ('Details', {
            'fields': ('technologies', 'order', 'date_created')
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'level', 'proficiency_percentage']
    list_filter = ['category', 'level']
    search_fields = ['name', 'category']
    ordering = ['-order', 'category']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'level')
        }),
        ('Proficiency', {
            'fields': ('proficiency_percentage', 'order')
        }),
    )


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'bio')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Links', {
            'fields': ('resume_link', 'github_profile', 'linkedin_profile', 'twitter_profile')
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one About entry
        return not About.objects.exists()
