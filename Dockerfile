FROM python:3.11-alpine3.19

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./src src

EXPOSE 8000

CMD ["python", "src/main.py"]