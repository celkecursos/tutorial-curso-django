from django.contrib import admin

from .models import PricingPlan

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_featured', 'situation')
