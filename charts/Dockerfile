FROM python:3.8

WORKDIR /app
COPY requirements.txt /app/requirementes.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirementes.txt

COPY . /app/

CMD bash -c "while true; do sleep 1; done"