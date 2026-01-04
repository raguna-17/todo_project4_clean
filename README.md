ToDoアプリ（Docker + Django）
プロジェクト概要

このプロジェクトは、入社アピール用に作成した Docker 環境で動く Django ベースの ToDo アプリです。
タスクの作成・編集・削除を行えるシンプルなアプリで、REST API を提供しています。
ローカルでは軽量な SQLite を使い、Render 本番環境では PostgreSQL を使う構成です。
DATABASE_URL 環境変数を切り替えることで、同じコードベースで両方の環境に対応しています。
さらに、pytest によるテストや カバレッジ測定も行っています。


技術スタック

バックエンド: Django
コンテナ管理: Docker / docker-compose
テスト: pytest, coverage
言語: Python 3.x

データベース: 
ローカル開発: SQLite（DATABASE_URL による設定可能）
本番 / Render: PostgreSQL（環境変数 DATABASE_URL で設定）


環境構築 / 起動手順
cd todo_project4_clean
cp .env.example .env
docker-compose exec web python manage.py migrate
docker-compose up --build


テストとカバレッジ
# Docker内でテスト実行
docker-compose exec web pytest

# カバレッジ測定
docker-compose exec web coverage run -m pytest
docker-compose exec web coverage report

pytestによる単体テストが実装済み
カバレッジ測定も可能で、コードの品質を確認できます


ディレクトリ構成（ファイル概要）

todo_project4_clean/
├─ todo/          # Djangoアプリ本体
│  ├─ templates/  # HTMLテンプレート
│  ├─ static/     # CSS/JS
│  ├─ api_views.py
│  └─ models.py
├─ Dockerfile
├─ docker-compose.yml
└─ requirements.txt



API エンドポイント一覧

| HTTP メソッド | URL | 説明 |
|---------------|-----|------|
| GET | /api/tasks/ | タスク一覧取得 |
| POST | /api/tasks/ | タスク作成 |
| GET | /api/tasks/{id}/ | タスク詳細取得 |
| PUT | /api/tasks/{id}/ | タスク更新（全体置換） |
| PATCH | /api/tasks/{id}/ | タスク更新（一部変更） |
| DELETE | /api/tasks/{id}/ | タスク削除 |



アピールポイント

Docker で環境を完全に分離し、即起動可能
Django + REST API の構築経験
pytestによるテストとカバレッジ測定で品質意識をアピール
将来的に API のドキュメント化やフロント連携も可能
