# Auth_RestApi
### Необходимо:
- Python
- PostgreSQL
#### или
- Docker
## Как запустить?
1. Клонируйте или скачайте проект.
2. Смените директорию на ```auth_restapi```
3. Создайте виртуальную среду: ```python -m venv venv```
4. Активируйте виртуальную среду: ОС Mac и Linux: ```source venv/bin/activate```, ОС Windows: ```venv\scripts\activate```
5. Установите зависимости: ```pip install -r requirements.txt```
6. Создайте файл ```setting.env``` с переменными окружения, который должен содержать в себе следующие значения:
- ```SECRET``` - секретный ключ
- ```DJANGO_ALLOWED_HOSTS=127.0.0.1 localhost``` - список разрешённых хостов
- ```POSTGRES_HOST=localhost``` - хост БД (по умолчанию ```localhost```)
- ```POSTGRES_DB``` - имя БД
- ```POSTGRES_USER``` - пользователь БД
- ```POSTGRES_PASSWORD``` - пароль БД
7. Запустите PostgreSQL.
8. Совершите миграцию базы данных: ```python manage.py migrate```
9. При необходимости создайте супер-пользователя: ```python manage.py createsuperuser```
10. Запустите сервер: ```python manage.py runserver```
11. Веб-сервис открыть по пути: http://127.0.0.1:8000/
## Как запустить с помощью Docker?
1. Клонируйте или скачайте проект.
2. Смените директорию на ```auth_restapi```
3. Создайте файл ```setting.env``` с переменными окружения, который должен содержать в себе следующие значения:
- ```SECRET``` - секретный ключ
- ```DJANGO_ALLOWED_HOSTS=127.0.0.1 localhost``` - список разрешённых хостов
- ```POSTGRES_DB``` - имя БД
- ```POSTGRES_USER``` - пользователь БД
- ```POSTGRES_PASSWORD``` - пароль БД
4. Создайте образ: ```docker-compose build```
5. Запустите базу данных ```docker-compose up -d db```
6. Запустите web-сервер ```docker-compose up -d web```
7. Совершите миграцию базы данных: ```docker-compose exec web python manage.py migrate```
8. Веб-сервис открыть по пути: http://127.0.0.1:8000/
