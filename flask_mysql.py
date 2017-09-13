# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = 2017 / 9 / 12
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Qaz123456789@localhost:3306/net_news?charset=utf8'
db = SQLAlchemy(app)

# 被讲师坑了，发现和导入数据库不一样，这里的变量要重新修改一下
class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    types = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(300),)
    author = db.Column(db.String(20),)
    view_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    is_valid = db.Column(db.Boolean)

    def __repr__(self):
        return '<News %r>' % self.title


@app.route('/')
def index():
    """ 新闻首页 """
    news_list = News.query.all()
    return render_template('index.html')


@app.route('/cat/<name>/')
def cat(name):
    """ 新闻的类别 """
    # 查询类别为name的新闻数据
    # query官方文档：http://docs.sqlalchemy.org/en/rel_1_1/orm/tutorial.html
    news_list = News.query.filter(News.types == name)
    return render_template('cat.html')


@app.route('/detail/<int:pk>/')
def detail(pk):
    """ 新闻详情信息 """
    news_obj = News.query.get(pk)
    return render_template('detail.html', news_obj=news_obj)

if __name__ == '__main__':
    # 调试模式
    # db.create_all()
    app.run(debug=True)
