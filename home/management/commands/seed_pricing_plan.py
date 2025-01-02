# BaseCommand: Classe base para criar comandos personalizados no Django. Ao herdar dessa classe, pode ser criado comandos que são executados pelo manage.py no terminal.
from django.core.management.base import BaseCommand
# PricingPlan: Importar o modelo PricingPlan da aplicação courses. O modelo representa a tabela no banco de dados onde os dados serão manipulados.
from home.models import PricingPlan

class Command(BaseCommand):
    # Mensagem de ajuda que descreve o propósito do comando
    help = 'Seed para cadastrar registro na tabela pricingplan'

    # O self permite que o método acesse os atributos e outros métodos definidos na classe.
    # *args: tupla de argumentos posicionais.
    # **kwargs: dicionário de argumentos nomeados. 
    def handle(self, *args, **kwargs):
        # Criar a lista de planos com os dados a serem cadastrados
        pricing_plan = [
            {
                'title': 'Gratuito',
                'price': '0',
                'period': 'mês',
                'description': 'Controle de despesas básicas<br>Relatórios mensais simples<br>1 conta bancária vinculada<br>Suporte via e-mail<br>',
                'title_btn': 'Comece Agora',
                'link_btn': 'https://celke.com.br/',
            },
            {
                'title': 'Avançado',
                'price': '19',
                'period': 'mês',
                'description': 'Gerenciamento completo de despesas<br>Relatórios detalhados e gráficos<br>Até 5 contas bancárias vinculadas<br>Suporte prioritário via e-mail<br>',
                'title_btn': 'Assinar Agora',
                'link_btn': 'https://celke.com.br/blog',
                'is_featured': True
            },
            {
                'title': 'Empresarial',
                'price': '49',
                'period': 'mês',
                'description': 'Controle de fluxo de caixa<br>Relatórios personalizados<br>Contas e cartões ilimitados<br>Suporte completo (telefone e e-mail)<br>',
                'title_btn': 'Fale Conosco',
                'link_btn': 'https://celke.com.br/contato',
            },
        ]
        # Iterar sobre a lista de plano
        for pricing_plan_data in pricing_plan:
            # Atualiza o registro existente ou cria um novo com base no título do plano
            PricingPlan.objects.update_or_create(
                title=pricing_plan_data['title'], # Critério de busca: título do plano
                defaults=pricing_plan_data # Valores padrão para criar ou atualizar
            )

        # Exibir uma mensagem no terminal indicando o sucesso da operação
        self.stdout.write(self.style.SUCCESS('Plano adicionado com sucesso!'))