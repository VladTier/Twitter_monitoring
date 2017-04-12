from extensions import db
from flask_login import UserMixin


words_table = db.Table('user_words',
                       db.Column(
                           'user_id', db.Integer, db.ForeignKey('Users.id')),
                       db.Column(
                           'word_id', db.Integer, db.ForeignKey('Words.id')))

tweets_table = db.Table('user_tweets',
                       db.Column(
                           'user_id', db.Integer, db.ForeignKey('Users.id')),
                       db.Column(
                           'tweet_id', db.Integer, db.ForeignKey('Tweets.id')))


class Users(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(30))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    password = db.Column(db.String(120))
    username = db.Column(db.String(20))
    words_table = db.relationship('Words', secondary=words_table,
                                  backref=db.backref('users', lazy='dynamic'))
    tweets_table = db.relationship('Tweets', secondary=tweets_table,
                                  backref=db.backref('users', lazy='dynamic'))


class Tweets(db.Model):
    __tablename__ = 'Tweets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    geo = db.Column(db.String(250))
    Author = db.Column(db.String(60))
    text = db.Column(db.String(140))
    words = db.Column(db.String(30))


class Words(db.Model):
    __tablename__ = 'Words'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    word = db.Column(db.String(250), unique=True)




