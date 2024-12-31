from django.shortcuts import render
from .models import PricingPlan

# Create your views here.
def home(request):
    pricingplan = PricingPlan.objects.filter(situation=True).order_by('price')[:3]
    return render(request, 'home/home.html', { 'pricingplan': pricingplan})