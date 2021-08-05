FROM python:3.9.5-alpine
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# RUN ["python", "manage.py", "collectstatic"]

FROM nginx
COPY --from=0 /app/staticfiles /usr/share/nginx/html