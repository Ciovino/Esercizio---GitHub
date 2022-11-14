from flask import Flask, render_template

app = Flask(__name__)
posts = [
        {'id': 1, 'titolo': 'CSS', 'data': '2022-10-10', 'tag': 'css', 'contenuto': 'CSS sta per Cascading Style Sheet e in questo post ne parleremo meglio'},
        {'id': 2, 'titolo': 'HTML', 'data': '2022-11-14', 'tag': 'html', 'contenuto': 'HTML sta per HyperText Markup Language e in questo post ne parleremo meglio'}
    ]

@app.route('/')
def homepage():
    return render_template('HTML/homepage.html', posts=posts)

@app.route('/posts/<int:id>')
def singlepost(id):
    post = posts[id-1]

    return render_template('HTML/single.html', post=post)

@app.route('/about')
def presentazione():
    return render_template('HTML/presentazione.html')