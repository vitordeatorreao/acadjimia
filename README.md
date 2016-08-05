# acadjimia

This is a toy project required to take the Python Django certificate from the Jornada de Cursos Citi. This project's documentation may be written in Portuguese (Brazil).

Este é um projeto de exemplo requerido para tirar o certificado de Python Django na Jornada de Cursos do Citi.

Para rodar o projeto exemplo, crie um ambiente virtual utilizando o `virtualenv` com o Python 3 como padrão. 
Ative o ambiente virtual, mude para a pasta do projeto e digite os seguintes comandos:

```bash
$ pip install -r requirements.txt
```

Então, você pode baixar o [banco de dados de exemplo](https://www.dropbox.com/s/pimi81iqgb4tj8n/db.sqlite3?dl=0) 
ou rodar os comandos:

```bash
$ ./manage.py migrate
```

Por fim, rode:

```bash
$ ./manage.py runserver
```
