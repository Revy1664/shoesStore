Как запустить backend-сервер:

1. Сгенерировать SECRET_KEY на сайте: https://djecrety.ir/ и вставить его в .env файл
2. Создать базу данных Postgresql
3. Заполнить файл .env на основе .env_sample
4. Применить миграции: python manage.py migrate
5. Создание администратора: python manage.py createsuperuser
6. Запустить сервер: python manage.py runserver