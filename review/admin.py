from django.contrib import admin
from .models import review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(review)
class ReviewAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
