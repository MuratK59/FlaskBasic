from app import app
from flask import flash, redirect, render_template, url_for

from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'kullaniciadi' : 'Mahmut F'}
    baslik = 'Anasayfa F'
    gonderiler = [
        {
            'yazar' : "Murat",
            'baslik' : 'Python',
            'icerik' : 'bla bla bla'
        },
        {
            'yazar' : "Ahmet",
            'baslik' : 'Flask',
            'icerik' : 'Web Framework'
        },
    ]
    # return "Hello World!"
    # return '''
    #     <html>
    #         <head>
    #             <title>Anasayfa</title>
    #         </head>
    #         <body>
    #             <h1>Merhaba, ''' + user['kullaniciadi'] + '''</h1>
    #         </body>
    #     </html>
    # '''
    return render_template('home.html', baslik=baslik, user=user, gonderiler=gonderiler)


# @app.route("/login") #buna dekoratör deniyor
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Sign In', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me={}'. format(
            form.username.data, form.remember_me
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
