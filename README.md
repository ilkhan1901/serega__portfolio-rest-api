Проект лично для серёги.

<br>

В API доступны следующие данные :

`api/portfolios/`

`api/portfolios/<id>`

<br>

Пример json ответа для `portfolios/` :

```json
[

    {

        "title": "<название проекта>",

        "link": "<ссылка на проект>",

        "image": "http://localhost:8000/media/example.png",

        "published": "<да публикации проекта в формате гггг-мм-дд>"

    }

]
```

<br>
  
Установка проекта :

1)  `pip install -r requirements.txt`

2)  `cd server`

3)  `python manage.py makemigrations && python manage.py migrate`

4)  `python manage.py createsuperuser`

<br>

Запуск проекта :

`python manage.py runserver`

<br>

Целую, князь...