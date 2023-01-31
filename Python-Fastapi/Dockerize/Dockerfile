FROM python:3.9


WORKDIR /code


COPY ./requirements.txt .


RUN pip install --no-cache-dir --upgrade -r requirements.txt
# Cache enabled

COPY ./app ./app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]