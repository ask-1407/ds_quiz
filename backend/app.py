from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DB_PATH = "db/quiz.db"

# データベース接続用の関数
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)  # SQLiteデータベースに接続
    conn.row_factory = sqlite3.Row  # 結果を辞書形式で扱えるよう設定
    return conn

# クイズデータを提供するAPIエンドポイント
@app.route('/api/quizzes', methods=['GET'])
def get_quizzes():
    conn = get_db_connection()  # データベース接続を取得
    quizzes = conn.execute('SELECT * FROM quizzes').fetchall()  # 全てのクイズを取得
    conn.close()  # 接続を閉じる

    # データを整形してJSON形式で返す
    result = []
    for quiz in quizzes:
        result.append({
            "id": quiz["id"],
            "question": quiz["question"],
            "choices": eval(quiz["choices"]),  # JSON文字列をPythonのリストに変換
            "answer": quiz["answer"],
            "explanation": quiz["explanation"]
        })
    return jsonify(result)  # フロントエンドにJSONを返す

if __name__ == "__main__":
    app.run(debug=True)  # サーバーを起動
