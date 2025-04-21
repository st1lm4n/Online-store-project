# Online-store-project

Интернет-магазин для хранения и продажи плагинов, примеров кода и цифровых продуктов.  
Проект разработан на Django с использованием Bootstrap для стилизации.

---

## Установка и запуск

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

## Структура проекта:
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
