from dataclasses import dataclass
import sqlite3
from flask import Flask, abort


app = Flask(__name__)


@dataclass
class Article:
        id: int
        title: str
        text: str
        author: str


def get_all_articles() -> list[Article]:
    with sqlite3.connect('sqlite.db') as connection:
        execution_result = connection.execute(
            'SELECT id, title, text, author FROM article')
        return [Article(*values) for values in execution_result.fetchall()]


def get_article(article_id) -> Article:
    with sqlite3.connect('sqlite.db') as connection:
        execution_result = connection.execute('SELECT * FROM article WHERE id = ?', (article_id,))
        result = execution_result.fetchall()
    return Article(result[0])


@app.route('/')
@app.route('/articles')
def all_articles():
    return f'''<html>
   <head>
       <title>Articles APP</title>
   </head>
   <body>
       <h1>All Articles</h1>
       <ul>
           <li><a href="/article/Article 1">Article 1</li>
           <li><a href="/article/Article 2">Article 2</li>
           <li><a href="/article/Article 3">Article 3</li>
       </ul>
   </body>
</html>
'''


@app.route('/article/<int:article_id>')
def article_view(article_id: int):
    article = get_article(article_id)
    if article is None:
        abort(404, 'Article not found')
    return f'''
    <html>
        <head>
            <title>Articles APP</title>
        </head>
        <body>
            <a href="/articles">Main page</a>
            <h1>{article.title}</h1>
            <h3>Author: {article.author}</h3>
            <p>{article.text}</p>
        </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(port=8080, debug=True)



