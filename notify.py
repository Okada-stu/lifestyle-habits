"""
notify.py — Discordへの投稿

担当: オオイシ
このファイルはオオイシさん以外は編集しないでください。
"""

import os

import requests

# WebhookのURLはコードに直接書かないでください。
# .env に書き、.env.example にはキー名だけを書きます。
# URLが分かれば誰でも投稿できてしまうため、公開リポジトリに残すと実害があります。
WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

TIMEOUT_SECONDS = 10


def post(message):
    """Discordにメッセージを投稿する。成功したら True を返す。

    TODO(オオイシ)
      - requests.post(WEBHOOK_URL, json={"content": message}, timeout=TIMEOUT_SECONDS)
      - 失敗しても例外でアプリ全体を止めないこと（通知が落ちても記録は残す）
      - エラーを print するときに WEBHOOK_URL を一緒に出さないこと
        （ログに残ると漏れます）
    """
    raise NotImplementedError("TODO(オオイシ)")


def build_daily_message(user_id, date, minutes_by_category):
    """1日分の記録を投稿用の文章に組み立てる。

    表示名は categories.LABELS / categories.USER_LABELS を使ってください。
    """
    raise NotImplementedError("TODO(オオイシ)")
