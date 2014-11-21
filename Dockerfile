FROM python:2.7

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD src .

CMD ["python", "manage.py", "runserver"]
