from django.db import models

class PricingPlan(models.Model):
    """Modelo que represa um plano"""
    title = models.CharField(max_length=100, verbose_name="Título")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    period = models.CharField(max_length=50, verbose_name="Período")
    description = models.TextField(verbose_name="Descrição")
    title_btn = models.CharField(max_length=50, verbose_name="Texto do Botão")
    link_btn = models.URLField(max_length=200, verbose_name="Link do Botão")
    situation = models.BooleanField(default=True, verbose_name="Situação")
    is_featured = models.BooleanField(default=False, verbose_name="Destaque")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de edição")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Plano de Preço'
        verbose_name_plural = 'Planos de Preços'

class PlanFeature(models.Model):
    """Características disponíveis nos planos"""
    name = models.CharField(max_length=100, verbose_name="Nome da Característica")
    description = models.TextField(blank=True, verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de edição")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Característica'
        verbose_name_plural = 'Características'

class PricingPlanFeature(models.Model):
    """Associação entre planos e características"""
    pricing_plan = models.ForeignKey(PricingPlan, on_delete=models.CASCADE, verbose_name="Plano")
    feature = models.ForeignKey(PlanFeature, on_delete=models.CASCADE, verbose_name="Característica")
    value = models.CharField(max_length=100, blank=True, null=True, verbose_name="Valor")
    has_feature = models.BooleanField(default=False, verbose_name="Disponível")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de edição")

    def __str__(self):
        return f"{self.pricing_plan.title} - {self.feature.name}"
    
    class Meta:
        verbose_name = 'Característica do Plano'
        verbose_name_plural = 'Características dos Planos'

class ContentHome(models.Model):
    """Modelo que represa o conteúdo da página home"""
    title = models.CharField(max_length=100, verbose_name="Título")
    subtitle = models.CharField(max_length=255, verbose_name="Descrição")
    titlefeature = models.CharField(max_length=100, verbose_name="Título dos Recursos")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de edição")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Conteúdo'
        verbose_name_plural = 'Conteúdos'

