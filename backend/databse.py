import sqlite3

DB_PATH = "db/quiz.db"  # データベースファイルのパス

# データベースを初期化する関数
def initialize_db():
    conn = sqlite3.connect(DB_PATH)  # データベースに接続
    with open("backend/quiz_data.sql", "r") as f:  # SQLファイルを読み込む
        conn.executescript(f.read())  # SQLスクリプトを実行してテーブルを作成
    conn.commit()  # 変更を確定
    conn.close()  # 接続を閉じる

if __name__ == "__main__":
    initialize_db()  # 初期化を実行
    print("Database initialized.")  # 初期化完了メッセージを表示
