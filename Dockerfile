FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY main.py ./
COPY .env ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./main.py" ]
