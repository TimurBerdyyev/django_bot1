#  Установка библиотек

Скопируйте репозиторий
Установить библиотеки:`pip install -r requirements.txt`

## Поменять базу данных, TOKEN_API телеграмм бота, ID администратора телеграмм бота, SECRET_KEY Django

Переименуйте файл `.env.envs` на `.env`

## Сделайте миграции
Напишите эти команды: `python manage.py makemigrations`  `python manage.py migrate` 
`python manage.py createsuperuser`

## Запуск бота
Чтобы запустить Django напишитите : `python manage.py runserver`
Чтобы запустить телеграмм бота напишите: `python manage.py bot`