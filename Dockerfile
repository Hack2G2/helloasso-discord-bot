FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt .
COPY main.py .
COPY utils/ .
COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "./main.py" ]
