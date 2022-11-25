from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    con = sql.connect("questions.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from questions")
    data = cur.fetchall()
    return render_template("index.html", datas=data)


@app.route("/add_question", methods=['POST', 'GET'])
def add_question():
    if request.method == 'POST':
        question = request.form['question']
        answer = request.form['answer']
        con = sql.connect("questions.db")
        cur = con.cursor()
        cur.execute(
            "insert into questions(question,answer) values (?,?)", (question, answer))
        con.commit()
        flash('question added', 'success')
        return redirect(url_for("index"))
    return render_template("add_question.html")


@app.route("/edit_question/<string:id>", methods=['POST', 'GET'])
def edit_question(id):
    if request.method == 'POST':
        question = request.form['question']
        answer = request.form['answer']
        con = sql.connect("questions.db")
        cur = con.cursor()
        cur.execute(
            "update questions set question=?,answer=? where id=?", (question, answer, id))
        con.commit()
        flash('question updated', 'success')
        return redirect(url_for("index"))
    con = sql.connect("questions.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from questions where id=?", (id,))
    data = cur.fetchone()
    return render_template("edit_question.html", datas=data)


@app.route("/delete_question/<string:id>", methods=['GET'])
def delete_question(id):
    con = sql.connect("questions.db")
    cur = con.cursor()
    cur.execute("delete from questions where id=?", (id,))
    con.commit()
    flash('question deleted', 'warning')
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.secret_key = 'admin123'
    app.run(debug=True)
