# Веб-сервис для управления движением денежных средств (ДДС)

## Описание проекта

Веб-сервис для управления движением денежных средств (ДДС) предназначен для учета, управления и анализа денежных операций. Пользователи могут создавать, редактировать, удалять и просматривать записи о поступлениях и списаниях денежных средств с учетом параметров, таких как дата, статус, тип, категория, подкатегория, сумма и комментарий.

## Инструкция по запуску

Клонирование проекта 
```bash
  git clone https://github.com/tch619/cash_flow
  cd cash_flow_django
```

Установка вирутального окружения и зависимостей
```bash
python -m venv venv
source venv/bin/activate  # для Linux/MacOS
venv\Scripts\activate  # для Windows
pip install -r requirements.txt
```

Генерация secret_key/

```bash
создайте файл .env и создайте в нем переменную SECRET_KEY
python manage.py shell
from django.core.management import utils
utils.get_random_secret_key()
и присваиваем его (SECRET_KEY=YOUR_SECRET_KEY)
```


Настройка миграций для бд 
```bash
python manage.py makemigrations
python manage.py migrate
```

Загрузите fixtures
```bash
python manage.py loaddata initual_statuses.json initial_types.json

```

Создание суперюзера
```bash
python manage.py createsuperuser
```

Запуск сервера
```bash
python manage.py runserver
```


# Заключение

Этот проект представляет собой веб-приложение для учета и управления движением денежных средств с удобным пользовательским интерфейсом. Мы использовали Django для бэкенда и django-jazzmin для улучшения интерфейса админки. Важно отметить, что в приложении учтены все необходимые зависимости между типами, категориями и подкатегориями, а также реализована валидация данных как на клиентской, так и на серверной стороне.