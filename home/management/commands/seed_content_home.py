# BaseCommand: Classe base para criar comandos personalizados no Django. Ao herdar dessa classe, pode ser criado comandos que são executados pelo manage.py no terminal.
from django.core.management.base import BaseCommand
# ContentHome: Importar o modelo ContentHome da aplicação home. O modelo representa a tabela no banco de dados onde os dados serão manipulados.
from home.models import ContentHome

class Command(BaseCommand):
    # Mensagem de ajuda que descreve o propósito do comando
    help = 'Seed para cadastrar registro na tabela ContentHome'

    # O self permite que o método acesse os atributos e outros métodos definidos na classe.
    # *args: tupla de argumentos posicionais.
    # **kwargs: dicionário de argumentos nomeados. 
    def handle(self, *args, **kwargs):
        # Criar a lista de planos com os dados a serem cadastrados
        content_home = {
            'title': 'Nossos Planos',
            'subtitle': 'Escolha o plano que melhor se adapta às suas necessidades e alcance o controle financeiro que você merece. Comparamos os recursos de cada plano para que você encontre a solução ideal, desde opções básicas até funcionalidades avançadas para sua empresa.',
            'titlefeature': 'Compare os Planos',
        }
        
        # Iterar sobre a lista de plano
        # for content_home_data in content_home:
            # Atualiza o registro existente ou cria um novo com base no título
        ContentHome.objects.update_or_create(
            title=content_home['title'], # Critério de busca: título
            defaults=content_home # Valores padrão para criar ou atualizar
        )

        # Exibir uma mensagem no terminal indicando o sucesso da operação
        self.stdout.write(self.style.SUCCESS('Conteúdo da página inicial adicionado com sucesso!'))