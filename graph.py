"""
graph.py — グラフ画像の生成

担当: オオイシ
このファイルはオオイシさん以外は編集しないでください。

JavaScriptを使わないため、matplotlib で画像ファイルを作り、
HTMLの img タグで表示します。
"""

import matplotlib

# ↓ この2行の順番が重要です。
#   use("Agg") を pyplot の import より前に書かないと、画面のない環境（EC2）で
#   「画面がない」というエラーになって落ちます。手元のWindowsでは動くのに
#   EC2に上げた瞬間に動かなくなる、という事故の原因になります。
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

import categories

# 画像の出力先。この中身はGit管理外です（毎回作り直すため）
GRAPH_DIR = "static/graphs"


def _setup_japanese_font():
    """ラベルの日本語が □□□（豆腐）になるのを防ぐ。

    matplotlib の初期設定のフォントは日本語を持っていません。
    Windows なら 'Meiryo'、EC2(Amazon Linux) なら別のフォントを入れて指定します。
    EC2側の準備はオカダが行います。
    """
    plt.rcParams["font.family"] = ["Meiryo", "IPAexGothic", "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False


def make_pie(user_id, date_from, date_to):
    """期間内のカテゴリ別時間を円グラフにして保存する。

    戻り値: 作った画像のファイル名（例 'pie_okada_20261019.png'）
            app.py はこの名前をそのまま img タグに入れます。

    TODO(オオイシ)
      1. db.fetch_records(user_id, date_from, date_to) でデータを取る
      2. カテゴリごとに minutes を合計する（表示名は categories.LABELS を使う）
      3. plt で円グラフを描き、GRAPH_DIR に保存する
      4. plt.close() を必ず呼ぶ（呼ばないと図が溜まってメモリを食い続けます）

    ファイル名に日付や利用者名を入れてください。毎回同じ名前にすると、
    ブラウザが古い画像をキャッシュして「更新したのに前のグラフが出る」
    という症状になります。
    """
    raise NotImplementedError("TODO(オオイシ)")
