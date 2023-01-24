FROM python:3.10.0-alpine
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 1957
CMD ["python", "app.py"]