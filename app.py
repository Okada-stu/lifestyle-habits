"""
app.py — Flask本体。画面の入口（ルーティング）

担当: ナカムラ
このファイルはナカムラさん以外は編集しないでください。

JavaScriptは使いません。合計時間の検証はすべてこのファイル（サーバー側）で行います。
"""

from flask import Flask, render_template, request, redirect, url_for

import categories
import db

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("input_form"))


@app.route("/input")
def input_form():
    """入力画面を表示する。"""
    return render_template(
        "input.html",
        categories=categories.CATEGORIES,
        choices=categories.CHOICE_MINUTES,
        error=None,
    )


@app.route("/record", methods=["POST"])
def record():
    """入力を受け取って保存する。

    TODO(ナカムラ)
      1. request.form から各カテゴリの値（分・文字列で届く）を受け取り int に直す
         フォームの name 属性は categories.py のキー（sleep, school, ...）に合わせる
      2. 合計を検証する
           合計 > 1440  -> 保存せず input.html を再表示し error を渡す
           合計 <= 1440 -> 残りを 'other' に入れて db.save_day() を呼ぶ
      3. 保存できたら /list へリダイレクトする
    """
    raise NotImplementedError("TODO(ナカムラ)")


@app.route("/list")
def record_list():
    """一覧とグラフを表示する。

    TODO(ナカムラ)
      - db.fetch_records() で記録を取り出して表に出す
      - グラフは graph.py が作った画像を img タグで表示する
        （ファイル名は graph.make_pie() の戻り値を使う。自分で作らない）
    """
    raise NotImplementedError("TODO(ナカムラ)")


if __name__ == "__main__":
    # 開発中だけこの起動方法を使います。
    # 本番(EC2)では gunicorn から起動します -> ops/NOTES.md
    db.init_db()
    app.run(debug=True)
