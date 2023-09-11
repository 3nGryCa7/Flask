from flask import Flask, render_template
from view_form import UserForm
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def user():
    form = UserForm()
    # 使用flask_wtf中的validate_on_submit()方法，判断表單是否提交(method='POST')並且驗證通過
    if form.validate_on_submit():
        return 'Success Submit'
    # 否則是method='GET'
    return render_template('user.html', form=form)

if __name__ == '__main__':
    key = os.urandom(256)
    app.config['SECRET_KEY'] = key
    app.run(debug=True)