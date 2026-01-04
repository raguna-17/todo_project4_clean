ToDoアプリ（Docker + Django）

## プロジェクト概要

このプロジェクトは、入社アピール用に作成した Django ベースの ToDo アプリです。

- GitHub: [https://github.com/raguna-17/todo_project4_clean]
- Render 本番環境: [https://todo-project4-clean.onrender.com]

Docker 環境で動作し、以下の特徴があります:

- タスクの作成・編集・削除が可能
- タスクの順番をドラッグ＆ドロップで入れ替え可能
- REST API を提供
- ローカルでは SQLite、本番（Render）では PostgreSQL を使用
- DATABASE_URL の切り替えで同じコードベースで両環境に対応
- pytest によるテストとカバレッジ測定済み



## 技術スタック

バックエンド: Django
コンテナ管理: Docker / docker-compose
テスト: pytest, coverage
言語: Python 3.x

データベース: 
ローカル開発: SQLite（DATABASE_URL による設定可能）
本番 / Render: PostgreSQL（環境変数 DATABASE_URL で設定）


## 環境構築 / 起動手順
```bash
cd todo_project4_clean
cp .env.example .env
docker-compose exec web python manage.py migrate
docker-compose up --build
```

## テストとカバレッジ

```bash
# Docker内でテスト実行
docker-compose exec web pytest
# カバレッジ測定
docker-compose exec web coverage run -m pytest
docker-compose exec web coverage report
```

pytestによる単体テストが実装済み
カバレッジ測定も可能で、コードの品質を確認できます


## ディレクトリ構成（ファイル概要）

todo_project4_clean/
├─ todo/          
│  ├─ templates/  
│  ├─ static/     
│  ├─ api_views.py
│  └─ models.py
├─ Dockerfile
├─ docker-compose.yml
└─ requirements.txt



## API エンドポイント一覧

| HTTP メソッド | URL | 説明 |
|---------------|-----|------|
| GET | /api/tasks/ | タスク一覧取得 |
| POST | /api/tasks/ | タスク作成 |
| GET | /api/tasks/{id}/ | タスク詳細取得 |
| PUT | /api/tasks/{id}/ | タスク更新（全体置換） |
| PATCH | /api/tasks/{id}/ | タスク更新（一部変更） |
| DELETE | /api/tasks/{id}/ | タスク削除 |



## アピールポイント

- **GitHub リポジトリや本番環境URLを README で共有済み**
- Docker で環境を完全に分離しており、クローン後すぐに起動可能
- Django + REST API の構築経験をアピール
- pytest によるテスト・カバレッジ測定で品質意識を示す
- タスクの並び替え機能で UI/UX も考慮  
  （タスクをクリック＆ドラッグで自由に並び替え可能）

