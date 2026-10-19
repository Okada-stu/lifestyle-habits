"""
categories.py — カテゴリと利用者の定義

担当: オカダ（変更には4人の合意が必要）

このファイルは4人全員が import して使います。
各自が自分のファイルにカテゴリ名を直接書くと、表記揺れ
（「スマホ」と「スマホ・動画・SNS」）でデータが分裂します。
"""

# ===== カテゴリ =====
# 入力画面に並ぶ順に定義する
CATEGORIES = [
    ("sleep",  "睡眠"),
    ("school", "学校"),
    ("study",  "勉強・自習"),
    ("life",   "生活"),
    ("move",   "移動"),
    ("phone",  "スマホ・動画・SNS"),
    ("fun",    "娯楽"),
]

# 「その他」は利用者が入力しない。サーバー側で残り時間を自動計上する
OTHER = ("other", "その他")

# 表示名を引くための辞書  例: LABELS["sleep"] -> "睡眠"
LABELS = dict(CATEGORIES + [OTHER])

# DBに入れてよいキーの一覧（検証用）
VALID_KEYS = set(LABELS.keys())


# ===== 利用者 =====
# DBの user_id に入る値。画面に出すのは表示名
USERS = [
    ("abe",      "アベ"),
    ("oishi",    "オオイシ"),
    ("okada",    "オカダ"),
    ("nakamura", "ナカムラ"),
]

USER_LABELS = dict(USERS)
VALID_USER_IDS = set(USER_LABELS.keys())


# ===== 時間の単位 =====
# 時間は「分」の整数で持つ。0.5時間 = 30分、24時間 = 1440分
STEP_MINUTES = 30
MAX_MINUTES = 24 * 60  # 1440

# 入力の選択肢（分）。0 〜 1440 を 30 刻み
CHOICE_MINUTES = list(range(0, MAX_MINUTES + 1, STEP_MINUTES))


def to_hours_text(minutes):
    """分 -> 画面表示用の文字列。 450 -> '7.5'"""
    return f"{minutes / 60:.1f}"
