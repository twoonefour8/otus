FROM python:3.9-buster

WORKDIR /www
COPY . ./
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]