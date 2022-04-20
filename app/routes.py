from app import app
from flask import render_template

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