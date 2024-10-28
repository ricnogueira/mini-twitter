# mini-twitter

## Install Project (Comandos Linux)

1 - Clone o Projeto:
```
git clone https://github.com/ricnogueira/mini-twitter.git
```
2 - Entre na pasta:
```
cd mini-twitter
```
3 - Crie o virtual env:
```
python3 -m venv .venv
```
4 - Ative o virtual env:
```
source .venv/bin/activate
```
5 - Instale as dependências:
```
pip install -r requirements.txt 
```
6 - Crie as pastas static/images e images na raiz do projeto:
```
mkdir -p static/images
mkdir images
```
7 - Crie a estrutura do banco de dados:
```
python3 manage.py migrate
```
8 - Crie o usuário para logar no admin do Django (opcional):
```
python3 manage.py createsuperuser
```
9 - Inicie o servidor:
```
python manage.py runserver 
```
10 - Acesse o admin com o usuário e senha criados no passo anterior (opcional):
http://127.0.0.1:8000/admin/

## Link para a documentação da API (Postman)
```
https://www.postman.com/ricaleno/twitter/request/b92kdid/obtain-token
```

