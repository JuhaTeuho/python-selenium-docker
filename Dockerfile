
FROM python:3.9

COPY . /app
WORKDIR /app

RUN apt update && apt install -y \
    chromium \
    chromium-driver

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ENV RUNNING_IN_CONTAINER True

CMD ["python", "-u", "./main.py"]