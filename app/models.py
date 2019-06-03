from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__= 'users'
    id=db.Column(db.Integer,primary_key =True)
    username = db.Column(db.String(255))
    email=db.Column(db.String(255),unique=True,index = True)
    pass_hash =db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password Attribute')

    @password.setter
    def password(self,password):
        self.pass_hash =generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.pass_hash,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):

        return 'User {self.username}'

class Comments(db.Model):
    __tablename__ ='comments'
    id = db.Column(db.Integer,primary_key= True)
    name=db.Column(db.String(255))
    blog=db.relationship('Blog',backref='comments',lazy='dynamic')

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls):
        '''
        Function that queries the Groups Table in the database and returns all the information from the Groups Table
        Returns:
            groups : all the information in the groups table
        '''

        comments = Comments.query.all()

        return comments


class Blog(db.Model):
    __tablename__='blogs'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255))
    description=db.Column(db.String)
    like = db.Column(db.Integer)
    dislike = db.Column(db.Integer)
    comments_id =db.Column(db.Integer,db.ForeignKey("comments.id"))


    def save_blog(self):
        db.session.add(self)
        db.session.commit()

        
    @classmethod
    def get_blogs(cls):
        '''
        gets blogs from the database
        '''
        blogs=Blog.query.all()
        return blogs