# Computer Club Web

## Установка

```bash
pip install -r requirements.txt
# Настройте PostgreSQL (computer_club_new)
python manage.py seed_data
python manage.py runserver
```

## Роли (как в БД)

| UI       | role в БД     | club_id | Логин   | Пароль     | Возможности                    |
|----------|---------------|---------|---------|------------|--------------------------------|
| Admin    | `main_admin`  | NULL    | admin   | admin123   | Тарифы, услуги, менеджеры      |
| Manager  | `club_admin`  | обязателен | manager | manager123 | Компьютеры, клиенты, сессии |

Ограничение БД:
```sql
CHECK (
  (role = 'main_admin' AND club_id IS NULL)
  OR
  (role = 'club_admin' AND club_id IS NOT NULL)
)
```

## Справочники (seed_data)

- Зоны: Standart, VIP
- Статусы ПК: Активен, Не активен
- Статусы сессий: Активна, Завершена, Отменена, Забронирована
