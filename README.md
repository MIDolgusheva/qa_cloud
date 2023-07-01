#### MAIN IDEA
Этот проект содержит тесты для методов GET, POST, DELETE к https://jsonplaceholder.typicode.com

#### PREREQUISITES
1. Скачайте репозиторий
2. Cоздайте виртулальное окружение и активируйте его
2. При необходимости, установите pip
3. Установите  [allure2]( https://docs.qameta.io/allure/#_installing_a_commandline) и настройте переменную среды JAVA_HOME
#### RUN

2. Для запуска тестов локально: 

* Перейдите в корневую папку проекта 

Linux:

* `./run.sh` 

Windows: 

* `.\run.bat`

3. Для запуска тестов в docker:

* `docker build -t tests .`

* `docker run --rm --mount type=bind,src=<путь_до_проекта>,target=/qa/ tests`

