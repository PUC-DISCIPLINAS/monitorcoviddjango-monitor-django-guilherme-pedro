# Dashboard COVID no mundo

Uma tabela onde se pode cadastrar, editar e excluir dados dos países em relação a COVID 19.
Os dados na tabela são:
País: o nome do país;
Casos confirmados: a soma de mortes e recuperados;
Recuperados: pessoas que se curaram da covid;
Mortes: pessoas que faleceram devido a covid.

## Integrantes

* Guilherme Augusto Gomes Cunha
* Pedro Henrique Magalhaes Silva

## Orientadores

* Hugo Bastos de Paula

## Instruções de utilização

Caso o usuário 'admin' não esteja cadastrado utilize o comando 'python manage.py createsuperuser', caso o usuário admin for o que está cadastrado o login é 'admin' e senha '123'. Caso seja necessário fazer as migrações os comandos são:
-python manage.py makemigrations core
-python manage.py migrate core
-python manage.py migrate

Seguindo esses passos a aplicação estará pronta para rodar, digite o comando python manage.py runserver e entrar em http://localhost:8000