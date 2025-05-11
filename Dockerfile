FROM python:3.12-slim

RUN pip install --no-cache-dir fastapi uvicorn xgboost 

WORKDIR /app

COPY main.py   /app/main.py
COPY model.pkl /app/model.pkl

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

