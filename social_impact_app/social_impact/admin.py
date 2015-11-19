from django.contrib import admin

from social_impact.models import Answers, Complaint


class AnswersInline(admin.TabularInline):
    model = Answers
    extra = 3


class ComplaintAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['complaint_text']}),
        ('Date information', {'fields': ['pub_date'],
                              'classes': ['collapse']}),
    ]
    inlines = [AnswersInline]
    list_filter = ['pub_date']
    search_fields = ['complaint_text']
    list_display = ('complaint_text', 'pub_date', 'was_published_recently')

admin.site.register(Complaint, ComplaintAdmin)
