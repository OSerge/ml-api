# ml-api

## Использование

1. Склонируйте проект: `git clone https://github.com/OSerge/ml-api.git`
2. Перейдите в директорию проекта: `cd ml-api/`
3. Соберите docker-образ: `docker build -t ml-api .`
4. Запустите его: `docker run --rm -p 8000:8000 ml-api`
5. Проверьте ответ модели тестовым запросом: `curl -X 'POST' 'http://localhost:8000/predict' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"features": [0.1, 0.5]}' `. Ответ должен быть: `{"prediction":1.0,"status":"success"}`
6. Аналогичные запросы можно делать непосредственно в web-интерфейсе Swagger, который запускается вместе с FastAPI. Для этого перейдите по адресу `http://localhost:8000/docs#/default/predict_predict_post`, нажмите кнопку `Try it out` и введите два `float`-числа в списке `features`, например `{"features": [0.4, 0.5]}`. Нажмите `Execute` и в секции `Responses` увидите ответ сервера с результатом работы модели.
