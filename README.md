## Requisitos

* Python 3 ou superior - Conferir a versão: python --version
* Django 5 ou superior - Conferir a versão: django-admin --version
* MySQL 8 ou superior - Conferir a versão: mysql --version
* GIT - Conferir a instalação: git -v

## Como rodar o projeto baixado

Criar o ambiente virtual.
```
python -m venv venv
```

Ativar o ambiente virtual.
```
venv\Scripts\activate
```

Instalar as dependências.
```
pip install -r requirements.txt
```

Alterar no arquivo "settings.py" as credenciais do banco de dados<br>
```
'ENGINE': 'django.db.backends.mysql',
'NAME': 'nome-do-banco-de-dados',
'USER': 'usuario-do-banco-de-dados',
'PASSWORD': 'senha-do-usuario-do-banco-de-dados',
'HOST': 'localhost',
'PORT': 3306,
```

Executa as migration para criar as tabelas.
```
python manage.py migrate
```

Rodar o projeto.
```
python manage.py runserver
```

Acessar o conteúdo padrão do Python.
```
http://127.0.0.1:8000
```

Criar um super usuário.
```
python manage.py createsuperuser
```
```
Usuário (leave blank to use 'cesar'): admin
Endereço de email: cesar@celke.com.br
Password: 123456A#
Password (again): 123456A#
```

Acessar o sistema administrativo padrão do Python.
```
http://127.0.0.1:8000/admin
```

Usuário: admin
Senha: 123456A#

## Sequencia para criar o projeto

Instalar o Django.
```
pip install Django
```

Criar o projeto com Django.
```
django-admin startproject admin .
```

Rodar o projeto.
```
python manage.py runserver
```

Criar a base de dados.
```
CREATE DATABASE celke CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Instalar o conector MySQL.
```
pip install mysqlclient
```

Alterar no arquivo "settings.py" as credenciais do banco de dados<br>
```
'ENGINE': 'django.db.backends.mysql',
'NAME': 'nome-do-banco-de-dados',
'USER': 'usuario-do-banco-de-dados',
'PASSWORD': 'senha-do-usuario-do-banco-de-dados',
'HOST': 'localhost',
'PORT': 3306,
```

Executa as migration para criar as tabelas.
```
python manage.py migrate
```

Criar um super usuário.
```
python manage.py createsuperuser
```
```
Usuário (leave blank to use 'cesar'): admin
Endereço de email: cesar@celke.com.br
Password: 123456A#
Password (again): 123456A#
```

Acessar o sistema administrativo padrão do Python.
```
http://127.0.0.1:8000/admin
```

Criar novo app.
```
python manage.py startapp nome-do-app
```
```
python manage.py startapp transactions
```

Criar a migrations.
```
python manage.py makemigrations nome-do-app --name nome-da-migrations
```
```
python manage.py makemigrations transactions --name financial_transactions
```

Criar o ambiente virtual.
```
python -m venv venv
```

Ativar o ambiente virtual.
```
venv\Scripts\activate
```

Gerar o arquivo com as dependências.
Após instalar a dependência, execute o comando abaixo.
```
pip freeze > requirements.txt
```
