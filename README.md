# Computer Club — Django сайт

Сайт компьютерного клуба, подключённый к PostgreSQL базе `computer_club_new`.

## Быстрый старт

1. Создайте виртуальное окружение:
```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/Mac
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` (скопируйте из `.env.example`) и укажите пароль от PostgreSQL.

4. Запустите сервер:
```bash
python manage.py runserver
```

5. Откройте http://127.0.0.1:8000/

## Страницы

- `/` — главная
- `/tariffs/` — тарифы (+ добавление/редактирование)
- `/services/` — услуги
- `/computers/` — компьютеры
- `/clients/` — клиенты
