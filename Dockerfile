FROM python:3-alpine
ADD requirements.txt .
ADD webapp pi-serve/
WORKDIR pi-serve/
RUN pip install -r requirements.txt
CMD python app.py
