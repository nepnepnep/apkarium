# Apkarium

**apkarium** — это лёгкое и безопасное хранилище APK-файлов, основанное на FastAPI.


## Установка

1. Создайте виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate  # для Linux/MacOS
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Запуск


### 1. Клонируйте репозиторий

```bash
git clone https://github.com/yourname/apkarium.git
cd apkarium
```

### 2. Создайте и активируйте виртуальное окружение

```bash
python -m venv .venv
source .venv/bin/activate  # Для Linux/Mac
.\.venv\Scripts\activate   # Для Windows
```

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```


### 4. Запустите FastAPI сервер

```bash
uvicorn apkarium.main:app --reload
```

По умолчанию FastAPI поднимается на:

```
http://127.0.0.1:8000
```

---

## 🧪 Документация API

Откройте в браузере:

```
http://127.0.0.1:8000/docs
```

Вы сможете:

- Загружать `.apk` файлы
- Скачивать их по ID
- Просматривать список доступных приложений

---

## 📁 Структура проекта

```
apkarium/
├── apkarium/
│   ├── main.py
│   ├── storage.py
│   └── models.py
├── storage/
│   └── apks/             # директория с файлами .apk
├── requirements.txt
└── README.md
```

---

## 🔒 Безопасность

По умолчанию проект работает без авторизации. Вы можете легко добавить:

- API Token (через заголовки)
- Авторизацию по JWT
- Подключение к Teleport через reverse proxy

---

## Структура проекта

- `apkarium.py` - основной файл приложения
- `requirements.txt` - файл зависимостей

## Требования

- Python 3.8+
- pip

## Лицензия

MIT
