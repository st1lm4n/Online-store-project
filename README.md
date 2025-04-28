# Online-store-project

Интернет-магазин для хранения и продажи плагинов, примеров кода и цифровых продуктов.  
Проект разработан на Django с использованием Bootstrap для стилизации.

---

## 🚀Установка и запуск

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/ваш-username/skystore.git
   cd skystore
   ```
2. **Создайте и активируйте виртуальное окружение:**
- Linux/macOS:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
- Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
3. **Установите зависимости:**
    ```
    pip install -r requirements.txt
    ```
4. **Выполните миграции:**
    ```bash
    python manage.py migrate
    ```
5. **Запустите сервер:**
    ```bash
    python manage.py runserver
    ```
6. **Откройте в браузере:**
   - Главная страница: http://localhost:8000/
   - Контакты: http://localhost:8000/contacts/

## 📂Структура проекта:
```
skystore/
├── config/              # Настройки Django
├── catalog/             # Приложение "Каталог"
│   ├── templates/      # HTML-шаблоны
│   ├── urls.py         # Маршруты приложения
│   └── views.py        # Контроллеры
├── venv/               # Виртуальное окружение
├── .gitignore          # Игнорируемые файлы
├── README.md           # Документация
├── requirements.txt    # Зависимости
└── manage.py           # Утилита Django
```
## 🌟Функциональность

- Главная страница:

  - Отображение карточек товаров.

  - Описание сервиса.

  - Навигация по категориям.

- Страница контактов:

    - Информация о компании (страна, ИНН, адрес).

    - Форма обратной связи (имя, телефон, сообщение).

## 🛠Технологии

- __Backend:__ Django 4.2

- __Frontend:__ Bootstrap 5.3 (подключен через CDN)

- __База данных:__ SQLite (для разработки)

## 🔗Маршруты (URL)
- `/` — Главная страница.

- `/contacts/` — Страница контактов.

## 📝GitFlow
- Ветка `main` — стабильная версия.

- Ветка `develop` — разработка.

- Функциональные ветки: `feature/*` (например, `feature/homework1`).

## 📌Дополнительно
- Форма обратной связи на странице контактов сохраняет данные (требуется настройка БД и views).

- Все URL-адреса заканчиваются на `/`.

© __2023 Online-store-project__

[Ссылка на репозиторий](https://github.com/st1lm4n/Online-store-project.git)