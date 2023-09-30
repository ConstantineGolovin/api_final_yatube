# api_final
API для проекта YaTube


## Использованные технологии:

Django Rest Framework
Djoser
Pillow
  
## Запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:ConstantineGolovin/api_final_yatube.git

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
## Примеры запросов:
Получение токена: http://127.0.0.1:8000/api/v1/jwt/create/
Получение публикаций: http://127.0.0.1:8000/api/v1/posts/
Список сообществ: http://127.0.0.1:8000/api/v1/groups/

## Об авторе
Автор проекта: Головин Константин Александрович, 68 когорта
