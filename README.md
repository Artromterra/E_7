# E_7

Создать директорию app, скачать в эту директорию папку tumblelog.

В директории создать виртуальное окружение python3 -m venv env, запустить: source env/bin/activate

Устанавливаем зависимости в виртуальное окружение pip3 install -r requirements.txt

Загружаем образ redis и mongo из реестра docker pull redis, docker pull mongo

Запускаем контейнер на основе образа: docker run -d -p 6379:6379 redis:5.0.7,  docker run -d -p 27017:27017 mongo:4.2.3

Переходим в директорию tumblelog, командой python manage.py runserver запускаем приложение.

Приложение работает на localhost:5000
