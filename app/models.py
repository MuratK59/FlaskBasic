from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

#ilk seferde migrations klasörünü oluşturmak için
#flask db init
#yazmamız gerekiyor.

#sonra ilk migrate yapmak için
#flask db migrate -m "Kullanıcı tablosu oluşturuldu"
#kodunu yazarız

#ancak bir fark olarak üstteki kod bu işleme hazır hale getirir
#flask db upgrade
#komutu ile tablo oluşacak