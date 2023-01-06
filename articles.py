from flask import Flask,jsonify,request
import csv
all_articles = []

with open("articles.csv") as f :
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked = []
disliked = []



app = Flask(__name__)
@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })

@app.route("/liked",methods = ["POST"])
def liked():
    article = all_articles[0]
    all_articles=all_articles[1:]
    liked_movies.append(article)
    return jsonify({
        "status":"success"
    }),201

@app.route("/disliked",methods = ["POST"])
def disliked():
    article = all_articles[0]
    all_articles=all_articles[1:]
    disliked.append(article)
    return jsonify({
        "status":"success"
    }),201



if __name__ == "__main__":
    app.run()