# YaMDb project
### Описание
Проект YaMDb собирает отзывы пользователей на различные произведения.
### Технологии
Python 3.7
Django 2.2.19
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
```
python -m venv venv
source venv/Scripts/activate
``` 
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Запустите сервер
```
python manage.py runserver
```
### Загрузка данных из csv файлов
- В папке api_yamdb/api_yamdb выполните команду:
```
python manage.py load_data
```
### Описание API
- API проекта находится по адресу http://127.0.0.1:8000/redoc/#section/Opisanie
### Пример запроса к API 
- CATEGORIES Получение списка всех категорий
```
GET CATEGORIES http://127.0.0.1:8000/api/v1/categories/
RESPONSE 200 (Удачное выполнение запроса)
[
  {
  "count": 0,
  "next": "string",
  "previous": "string",
   "results": [
                {
                 "name": "string",
                "slug": "string"
                }
                ...
              ]
  }
]
```

### Авторы
Антон Дёмин, Александр Набиев, Александр Фёдоров - факультет Бэкенд, когорта 26
