from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):

    title = StringField('Enter blog category',validators=[Required()])
    description= TextAreaField('blog description')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    name = TextAreaField('Enter comment.',validators = [Required()])
    submit = SubmitField('Submit')