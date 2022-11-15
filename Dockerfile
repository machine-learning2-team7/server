FROM --platform=linux/amd64 python:3.10

WORKDIR /code
COPY . /code
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
