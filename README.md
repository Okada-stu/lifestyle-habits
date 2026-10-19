# 生活習慣改善プログラム

1日の時間配分を記録・可視化するWebアプリ。4人開発。

- 詳しい仕様 → `docs/01_企画書.md`
- **AIに質問するときの前提テンプレ** → `docs/02_開発の共通前提.md`（毎回貼る）
- 環境構築の手順 → `docs/03_開発環境構築手順.md`

---

## 1. 誰がどのファイルを触るか

**自分の担当以外のファイルは触らないでください。** 直したい箇所があれば担当者に伝えます。

| ファイル / フォルダー | 担当 | 中身 |
| --- | --- | --- |
| `app.py` | ナカムラ | 画面の入口（ルーティング）・合計の検証 |
| `templates/` | ナカムラ | HTML（`base.html` / `input.html` / `list.html`） |
| `static/css/` | ナカムラ | CSS |
| `db.py` | アベ | DBの初期化・保存・取り出し |
| `graph.py` | オオイシ | グラフ画像の生成 |
| `notify.py` | オオイシ | Discordへの投稿 |
| `static/graphs/` | オオイシ | 生成したグラフ画像の置き場（Git管理外） |
| `ops/` | オカダ | デプロイ・運用（EC2） |
| `categories.py` | オカダ | カテゴリと利用者の定義（**変更は4人の合意が必要**） |
| `requirements.txt` | オカダ | 使うライブラリ（**追加したいときは先に相談**） |
| `docs/` | 全員 | 文書 |

別々のファイルなので、普通に作業していればGitの衝突は起きません。
衝突が起きるのは、上の表の「合意が必要」の2つを勝手に触ったときだけです。

---

## 2. 担当をまたぐ受け渡し（ここだけ守れば合流できる）

自分のファイルの中は自由に書いて構いません。守るのは次の3点だけです。

**1. DBを触るのは `db.py` だけ**

ナカムラさんとオオイシさんは SQL を書きません。`db.py` の関数を呼びます。

```python
db.save_day(user_id, date, {"sleep": 420, "school": 300, ...})   # 保存
db.fetch_records(user_id, "2026-10-13", "2026-10-19")            # 取り出し
```

**2. カテゴリ名と利用者IDは `categories.py` から取る**

自分のファイルに `"睡眠"` や `"sleep"` と直接書かないでください。表記揺れでデータが分裂します。

```python
import categories
categories.CATEGORIES   # [("sleep", "睡眠"), ...] 入力画面に並べる順
categories.LABELS       # {"sleep": "睡眠", ...} キー -> 表示名
```

**3. グラフは「オオイシさんが作り、ナカムラさんが貼る」**

```python
name = graph.make_pie(user_id, date_from, date_to)   # ファイル名を返す
```

`app.py` はこの戻り値を `list.html` に渡すだけです。画像を作りません。

---

## 3. はじめかた

```
git clone https://github.com/Okada-stu/lifestyle-habits.git
cd lifestyle-habits

python -m venv .venv
.venv\Scripts\activate            （Windows）

pip install -r requirements.txt
copy .env.example .env            （中身を書き込む）

python app.py                     → http://127.0.0.1:5000
```

いまの状態では、画面を開くと `NotImplementedError` が出ます。**それが正常です。**
各自が自分のファイルの `TODO` を埋めると動くようになります。

作業は自分のブランチで行い、`main` に直接pushしないでください（`docs/03` の7章）。

---

## 4. 注意点

**`app.db` と `.env` と `static/graphs/` の中身はGitに入りません**（`.gitignore` 済み）。
入れてしまうと、`app.db` は各自の記録が混ざって毎回衝突し、`.env` はDiscordのトークンが公開リポジトリに残り、グラフ画像は毎日作り直されるので差分が延々と出ます。

**`.env` は `git clone` では来ません。** 各自が `.env.example` をコピーして作ります。EC2上でも同じです。

**日本語を読み書きするときは `encoding="utf-8"` を明示してください。** Windowsでは省略すると cp932 になり、文字化けや例外の原因になります。

**グラフ画像のファイル名は毎回変えてください。** 同じ名前だとブラウザが古い画像をキャッシュし、「更新したのに前のグラフが出る」という症状になります。

**合計時間の検証はサーバー側（Python）で行います。** JavaScriptを使わない方針のため、入力中に画面で合計が自動更新されることはありません。保存ボタンを押した後にサーバーが判定します。

**`requirements.txt` にライブラリを足したいときは先に相談してください。** 黙って足すと、他の3人の手元で `ModuleNotFoundError` が出ます。

**AIが「`app.py` をこう書き換えて」と言ってきても、担当外なら従わないでください。** `docs/02` の4章のルール3です。
