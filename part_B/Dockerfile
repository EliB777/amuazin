#FROM ubuntu:latest
#LABEL authors="elibl"
FROM python:3.12-slim
ENTRYPOINT ["top", "-b"]

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#ENV PYTHONUNBUFFERED=1

CMD ["python", "-u", "part_B/test_3.py"]