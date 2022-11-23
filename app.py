from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_session import Session
from datetime import date

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)

posts = [
        {'id': 1, 'titolo': 'CSS', 'data': '2022-10-10', 'tag': 'css', 'contenuto': 'CSS sta per Cascading Style Sheet e in questo post ne parleremo meglio'},
        {'id': 2, 'titolo': 'HTML', 'data': '2022-11-14', 'tag': 'html', 'contenuto': 'HTML sta per HyperText Markup Language e in questo post ne parleremo meglio'}
    ]

@app.route('/')
def homepage():
    return render_template('homepage.html', posts=posts)

@app.route('/posts/<int:id>')
def singlepost(id):
    post = posts[id-1]
    
    return render_template('single.html', post=post)

@app.route('/about')
def presentazione():
    return render_template('presentazione.html')

@app.route('/admin')
def admin():
    session['admin'] = True
    flash('Sei amministratore', 'warning')
    return redirect(url_for('homepage'))

@app.route('/posts/new', methods=['POST', 'GET'])
def new_post():
    if request.method == 'POST':
        newPost = request.form.to_dict()

        # TODO: Rivalidare TUTTI i campi del form        
        # Controllo data
        if newPost.get('data') == '':
            # Inserisco data di default
            newPost['data'] = date.today()
        # Aggiungo l'immagine
        postImmagine = request.files.get('immagine')
        if postImmagine:
            postImmagine.save('static/Immagini/' + newPost.get('titolo').lower() + '.jpg')

        # Aggiungo id
        newPost['id'] = posts[-1]['id'] + 1

        # Aggiorno 'posts'
        posts.append(newPost)

        #app.logger.debug(request.form.get('titolo'))
        flash('Post creato correttamente', 'success')
        return redirect(url_for('homepage'))
    else:
        return render_template('new-post.html')