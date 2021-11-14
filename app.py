import csv
from flask import Flask, jsonify, request

app = Flask(__name__)

global all_articles
all_articles = []
liked_articles = []
not_liked_articles = []

with open('./data/articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]


@app.route('/get_article')
def get_article():
    return jsonify({
        'data': all_articles[0],
        'status': 'Success'
    }), 200

@app.route('/like_article', methods=['POST'])
def like_article():
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)

    print(liked_articles)

    return jsonify({
        'status': 'Success'
    }), 201

@app.route('/not_liked_article', methods=['POST'])
def not_liked_articles():
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)

    return jsonify({
        'status': 'Success'
    }), 201

if __name__ == '__main__':
    app.run(debug=True)