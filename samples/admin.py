from django.contrib import admin
from .models import Sample

@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('sample_id', 'subject_id', 'sample_type', 'status', 'collection_date')
    search_fields = ('sample_id', 'subject_id')
    list_filter = ('sample_type', 'status')
