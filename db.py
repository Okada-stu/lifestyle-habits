"""
db.py — DBの初期化・保存・取り出し

担当: アベ
このファイルはアベさん以外は編集しないでください。

------------------------------------------------------------------
【注意】下に書いてある関数名・引数・戻り値は「案」です。
10/18 の相談でアベさんが確定させてください。確定したらこのコメントを消します。
他の3人は、ここで確定した関数しか呼びません（SQLを自分で書かない）。
------------------------------------------------------------------
"""

import sqlite3

DB_PATH = "app.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS records (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id  TEXT    NOT NULL,
    date     TEXT    NOT NULL,              -- 'YYYY-MM-DD'
    category TEXT    NOT NULL,
    minutes  INTEGER NOT NULL,              -- 30の倍数
    UNIQUE (user_id, date, category)
);
"""


def connect():
    """DBに接続する。

    timeout=10 を付けてあります。4人が同時に保存したとき、SQLiteは
    書き込みを1人ずつしか通さないため、待たずに即エラーになるのを防ぎます。
    """
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row  # 結果を辞書のように扱えるようにする
    return conn


def init_db():
    """テーブルを作る（既にあれば何もしない）。アプリ起動時に1回呼ぶ。"""
    raise NotImplementedError("TODO(アベ)")


def save_day(user_id, date, minutes_by_category):
    """1人の1日分（8カテゴリ）をまとめて保存する。

    引数:
        user_id              : 'abe' など
        date                 : 'YYYY-MM-DD'
        minutes_by_category  : {'sleep': 420, 'school': 300, ...} 分の整数

    同じ user_id と date で2回目が来たら「上書き」です。
    INSERT ... ON CONFLICT (user_id, date, category) DO UPDATE を使います。
    """
    raise NotImplementedError("TODO(アベ)")


def fetch_records(user_id, date_from, date_to):
    """指定した利用者と期間の記録を取り出す。

    戻り値の案: [{'date': '2026-10-19', 'category': 'sleep', 'minutes': 420}, ...]
    （date_from / date_to は両端を含む）
    """
    raise NotImplementedError("TODO(アベ)")
