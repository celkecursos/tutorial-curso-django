# BaseCommand: Classe base para criar comandos personalizados no Django. Ao herdar dessa classe, pode ser criado comandos que são executados pelo manage.py no terminal.
from django.core.management.base import BaseCommand
# Importar o modelo PricingPlan, PlanFeature, PricingPlanFeature da aplicação home. O modelo representa a tabela no banco de dados onde os dados serão manipulados.
from home.models import PricingPlan, PlanFeature, PricingPlanFeature

class Command(BaseCommand):
    # Mensagem de ajuda que descreve o propósito do comando
    help = 'Seed para cadastrar registro nas tabelas PlanFeature, PricingPlanFeature'

    # O self permite que o método acesse os atributos e outros métodos definidos na classe.
    # *args: tupla de argumentos posicionais.
    # **kwargs: dicionário de argumentos nomeados. 
    def handle(self, *args, **kwargs):
        # Criar a lista de características com os dados a serem cadastrados
        features = [
            {"name": "Controle de despesas básicas", "description": "Permite o controle de despesas básicas."},
            {"name": "Relatórios detalhados", "description": "Geração de relatórios detalhados sobre finanças."},
            {"name": "Contas bancárias vinculadas", "description": "Número de contas bancárias que podem ser vinculadas."},
            {"name": "Gráficos e relatórios personalizados", "description": "Visualização de gráficos personalizados."},
            {"name": "Suporte via e-mail", "description": "Acesso ao suporte técnico via e-mail."},
            {"name": "Suporte prioritário", "description": "Prioridade no suporte técnico."},
            {"name": "Suporte completo (telefone e e-mail)", "description": "Suporte completo por telefone e e-mail."},
        ]

        # Iterar sobre a lista de características
        for features_data in features:
            PlanFeature.objects.get_or_create(**features_data)

        # Recuperar planos existentes
        gratuito = PricingPlan.objects.get(title="Gratuito")
        avancado = PricingPlan.objects.get(title="Avançado")
        empresarial = PricingPlan.objects.get(title="Empresarial")

        # Associar características aos planos
        plan_features = [
            # Gratuito
            {"pricing_plan": gratuito, "feature": PlanFeature.objects.get(name="Controle de despesas básicas"), "has_feature": True},
            {"pricing_plan": gratuito, "feature": PlanFeature.objects.get(name="Relatórios detalhados"), "has_feature": False},
            {"pricing_plan": gratuito, "feature": PlanFeature.objects.get(name="Contas bancárias vinculadas"), "value": "1"},
            {"pricing_plan": gratuito, "feature": PlanFeature.objects.get(name="Gráficos e relatórios personalizados"), "has_feature": False},
            {"pricing_plan": gratuito, "feature": PlanFeature.objects.get(name="Suporte via e-mail"), "has_feature": True},
            {"pricing_plan": gratuito, "feature": PlanFeature.objects.get(name="Suporte prioritário"), "has_feature": False},
            {"pricing_plan": gratuito, "feature": PlanFeature.objects.get(name="Suporte completo (telefone e e-mail)"), "has_feature": False},

            # Avançado
            {"pricing_plan": avancado, "feature": PlanFeature.objects.get(name="Controle de despesas básicas"), "has_feature": True},
            {"pricing_plan": avancado, "feature": PlanFeature.objects.get(name="Relatórios detalhados"), "has_feature": True},
            {"pricing_plan": avancado, "feature": PlanFeature.objects.get(name="Contas bancárias vinculadas"), "value": "Até 5"},
            {"pricing_plan": avancado, "feature": PlanFeature.objects.get(name="Gráficos e relatórios personalizados"), "has_feature": True},
            {"pricing_plan": avancado, "feature": PlanFeature.objects.get(name="Suporte via e-mail"), "has_feature": True},
            {"pricing_plan": avancado, "feature": PlanFeature.objects.get(name="Suporte prioritário"), "has_feature": True},
            {"pricing_plan": avancado, "feature": PlanFeature.objects.get(name="Suporte completo (telefone e e-mail)"), "has_feature": False},

            # Empresarial
            {"pricing_plan": empresarial, "feature": PlanFeature.objects.get(name="Controle de despesas básicas"), "has_feature": True},
            {"pricing_plan": empresarial, "feature": PlanFeature.objects.get(name="Relatórios detalhados"), "has_feature": True},
            {"pricing_plan": empresarial, "feature": PlanFeature.objects.get(name="Contas bancárias vinculadas"), "value": "Ilimitadas"},
            {"pricing_plan": empresarial, "feature": PlanFeature.objects.get(name="Gráficos e relatórios personalizados"), "has_feature": True},
            {"pricing_plan": empresarial, "feature": PlanFeature.objects.get(name="Suporte via e-mail"), "has_feature": True},
            {"pricing_plan": empresarial, "feature": PlanFeature.objects.get(name="Suporte prioritário"), "has_feature": True},
            {"pricing_plan": empresarial, "feature": PlanFeature.objects.get(name="Suporte completo (telefone e e-mail)"), "has_feature": True},
        ]

        # Iterar sobre a lista de relacionamento entre plano e característica
        for plan_features_data in plan_features:
            PricingPlanFeature.objects.get_or_create(**plan_features_data)

        # Exibir uma mensagem no terminal indicando o sucesso da operação
        self.stdout.write(self.style.SUCCESS('Características adicionadas com sucesso!'))