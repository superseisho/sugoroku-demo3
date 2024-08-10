FROM python:3.12.4
RUN pip install -r requirements.txt
CMD python server/main.py