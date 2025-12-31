#!/usr/bin/env bash
set -e

# マイグレーション適用
python manage.py migrate --noinput

# 静的ファイル収集（開発時は不要ならコメントアウト可）
python manage.py collectstatic --noinput 

# 引数で与えられたコマンドを実行（CMD のコマンドへ委譲）
exec "$@"