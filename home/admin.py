from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from .models import PricingPlan
from .models import PlanFeature
from .models import PricingPlanFeature

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_featured', 'situation')

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE}
    }

@admin.register(PlanFeature)
class PlanFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(PricingPlanFeature)
class PricingPlanFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
