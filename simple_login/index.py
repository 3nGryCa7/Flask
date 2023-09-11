from flask import Flask
from flask import redirect, url_for, request, jsonify, render_template, flash
import os

# jinja中的statement語法 : {% statement %}
# jinja中的python語法 : 使用 | 可以不報錯, ex: { var | upper } > 類同 str.upper(var)

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if check(request.form['username'], request.form['password']):
            # flash 可以將訊息由後端傳到前端
            flash('Login success', 'Welcome to the world!')
            return redirect(url_for('home', username=request.form.get('username')))
    # 用 url_for(function_name) 可以直接導向該function，而不需要寫死網址
    return render_template('login.html')

def check(username, password):
    return username == 'admin' and password == 'p@ssw0rd'


@app.route('/home/<username>')
def home(username):
    return render_template('index.html', username=username)

if __name__ == '__main__':
    # flash 需要設置key (使用os.urandom() 可以隨機生成)
    app.secret_key = os.urandom(256)
    # app.debug=True 是在開發環境的設置(正式環境絕對不會有)
    app.run(debug=True)