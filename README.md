
---

# Heartbeat API

**Описание:**  
Этот pet-проект представляет собой бекенд-сервис, реализованный с использованием FastAPI и SQLAlchemy, для управления записями на приёмы в медицинском учреждении. В системе реализованы модели пользователей (врачи и пациенты), а также модель встреч (Appointment) с двусторонними связями к врачам и пациентам. Проект организован по принципу разделения ответственности с использованием репозиториев, схем (Pydantic) и роутеров.

---

## Функциональность

- **Управление пользователями:**
   - Регистрация и управление данными пациентов и врачей.
   - Хранение и валидация данных через Pydantic-схемы.

- **Записи на приёмы (Appointment):**
   - Создание, обновление, удаление и получение информации о записях.
   - Возможность фильтрации встреч по врачу или пациенту.
   - Двусторонние связи (relationship) между встречами, врачами и пациентами.

- **Архитектура проекта:**
   - Использование паттерна Repository для работы с базой данных.
   - Чёткое разделение логики (модели, схемы, роутеры, репозитории, настройки и зависимости).

---

## Структура проекта

```
backend/
├── core/
│   ├── auth.py         # Функции для хэширования паролей
│   ├── db.py           # Настройка подключения к базе данных и создание таблиц
│   └── settings.py     # Настройки проекта (чтение переменных окружения)
├── tests/              # Тесты проекта (на данный момент пустой)
├── api/
│   ├── __init__.py
│   ├── main.py         # Точка входа приложения FastAPI
│   ├── routers/        # Маршруты API (patient, doctor, appointment)
│   │   ├── __init__.py
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── appointment.py
│   ├── repository/     # Репозитории для работы с базой данных
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── appointment.py
│   ├── dependencies/   # Зависимости для роутеров (на данный момент пустой)
│   ├── models/         # ORM-модели (User, Patient, Doctor, Appointment, Base)
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── user.py
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── appointment.py
│   └── schemas/        # Pydantic-схемы для валидации данных API
│       ├── __init__.py
│       ├── user.py
│       ├── patient.py
│       ├── doctor.py
│       └── appointment.py
```

---

## Установка и запуск

### Требования

- Python 3.10 или выше
- Установленные зависимости (указаны в файле `requirements.txt`)
- База данных (например, PostgreSQL, SQLite и т.п.)  
  **Пример переменных окружения (.env):**
  ```
  DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
  TEST_DATABASE_URL=postgresql+asyncpg://user:password@localhost/test_dbname
  ALGORITHM=HS256
  ```

### Установка зависимостей

```bash
python -m venv venv
source venv/bin/activate  # для Linux/macOS

pip install -r requirements.txt
```

### Запуск приложения

```bash
uvicorn backend.api.main:app --reload
```

После запуска сервер будет доступен по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).  
Эндпоинт `/` возвращает простой "Heartbeat".

---

## Описание API

### Эндпоинты пациентов

- **GET /patient/** – Получить список всех пациентов.
- **GET /patient/{patient_id:int}** – Получить данные конкретного пациента по ID.
- **POST /patient/** – Создать нового пациента.
- **PUT /patient/** – Обновить данные пациента.
- **DELETE /patient/** – Удалить пациента.

### Эндпоинты врачей

- **GET /doctor/** – Получить список всех врачей.
- **GET /doctor/{doctor_id:int}** – Получить данные конкретного врача по ID.
- **POST /doctor/** – Создать нового врача.
- **PUT /doctor/** – Обновить данные врача.
- **DELETE /doctor/** – Удалить врача.

### Эндпоинты встреч (Appointment)

- **GET /appointment/by_doctor/{doctor_id:int}** – Получить список встреч по ID врача.
- **GET /appointment/by_patient/{patient_id:int}** – Получить список встреч по ID пациента.
- **GET /appointment/by_id/{appointment_id:int}** – Получить данные конкретной встречи по ID.
- **POST /appointment/** – Создать новую встречу.
- **PUT /appointment/** – Обновить данные встречи.
- **DELETE /appointment/** – Удалить встречу.

---
