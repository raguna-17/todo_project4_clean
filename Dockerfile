FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# システム依存パッケージ
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential gettext \
    && rm -rf /var/lib/apt/lists/*

# Python依存関係
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install -r /app/requirements.txt

# アプリケーションコード
COPY todo/ /app/todo/
COPY config/ /app/config/
COPY manage.py /app/

# entrypoint
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# ポート
EXPOSE 8000

# ENTRYPOINT: マイグレーション / collectstatic を自動実行
ENTRYPOINT ["/entrypoint.sh"]

# CMD: Webサーバ起動のみ
CMD sh -c "gunicorn config.wsgi:application --bind 0.0.0.0:$PORT"
