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
