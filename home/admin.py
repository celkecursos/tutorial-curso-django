from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from .models import PricingPlan

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_featured', 'situation')

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE}
    }
