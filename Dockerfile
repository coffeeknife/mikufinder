FROM python:latest

COPY requirements.txt /
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

ADD src /src
CMD [ "python", "src/main.py" ]