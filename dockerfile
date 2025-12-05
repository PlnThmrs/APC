FROM python:3.11-slim

WORKDIR /apc

COPY . .

RUN pip install google-genai

CMD ["python", "app.py"]
