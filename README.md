### ОЦЕНКА ПОПУЛЯРНОСТИ БРЕНДА "Coca-Cola" в ВКонтакте
<hr>

Данный скрип получает статистические данные о количестве упоминаний бренда "Coca-Cola" в постах, в социальной сети "ВКонтакте".

Данные выводятся в виде графика количества упоминаний по дням, за последние 7 дней.

Запускают скрипт без параметров

```
    >> python.exe main.py
```	
В данной разработке инициализируються следующие переменные окружения:
- `VK_SERVICE_KEY` - переменная в которой храниться сервисный ключ доступа, необходимый для подключения к api сайта [www.vk.com](https://vk.com/dev/access_token?f=3.%20Сервисный%20ключ%20доступа)
		
Данные переменные инициализируються значениями заданными в .env файле.

Информацию о ходе выполнения скрипт пишет в файл log.txt, который должен находится в корневой папке скрипта.

#### КАК УСТАНОВИТЬ
<hr>

Для установки необходимо отредактировать файл .env, в котором заполнить ACCESS_TOKEN.

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:

```
    >> pip install -r requirements.txt
```

#### ЦЕЛЬ ПРОЕКТА
<hr>

Код написан в образовательных целях, для изучения возможностей api, на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).