from django.shortcuts import render
from .models import PricingPlan, PlanFeature, ContentHome

def home(request):
    # Recupera os planos ativos, ordenados pelo preço
    pricingplan = PricingPlan.objects.filter(situation=True).order_by('price')[:3]

    # Recupera todas as características
    features = PlanFeature.objects.all()

    # Prefetch das características para cada plano
    pricingplan = pricingplan.prefetch_related('pricingplanfeature_set__feature')

    # Recupera o conteúdo da página home
    content = ContentHome.objects.filter().first()

    context = {
        'pricingplan': pricingplan,
        'features': features,
        'content': content,
    }

    return render(request, 'home/home.html', context)