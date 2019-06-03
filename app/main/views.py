from flask import render_template,redirect,url_for,request
from . import main
from flask_login import login_required,login_user,logout_user
from ..models import Blog,Comments
from .forms import BlogForm,CommentForm
from ..import db



@main.route('/')
def index():
    title = 'Home'

    blogs = Blog.get_blogs()
    comments=Comments.get_comments()

    return render_template('index.html' ,title=title, blogs=blogs,comments=comments)

@main.route('/blog/new',methods=['GET','POST'])
@login_required
def new_blog():
    form= BlogForm()
    if form.validate_on_submit():
        title=form.title.data
        description=form.description.data
        like=0
        dislike=0
        new_blog=Blog(title=title,description=description,like=like,dislike=dislike)
        new_blog.save_blog()
        return redirect(url_for('.index'))

    title= 'Blogs'
    return render_template('new_blog.html',blog_form=form)

@main.route('/comment/new/', methods=['GET','POST'])
@login_required
def new_comment():

    '''
    View new comment route function that returns a page with a form to create a blog for the specified category
    '''
    comments = Comments.query.all()
    form =CommentForm()
    if form.validate_on_submit():
        name=form.name.data
        new_comment=Comments(name=name)
        new_comment.save_comment()

        return redirect(url_for('.index'))

    title = "New Comment"
    return render_template('new_comment.html', title=title, form=form,comments=comments)

@main.route('/blog_review/<int:id>',methods=['GET','POST'])

def blog_review(id):
    blogs = Blog.query.get_or_404(id)
    if request.args.get("like"):
        blogs.like = blogs.like+1

        db.session.add(blogs)
        db.session.commit()

        return redirect("/blog_review/{blog_id}".format(blog_id=blogs.id))

    elif request.args.get("dislike"):
        blogs.dislike = blogs.dislike+1

        db.session.add(blogs)
        db.session.commit()

        return redirect("/blog_review/{blog_id}".format(blog_id=blogs.id))

    title= 'Blogs'
    return render_template('blog_review.html',blogs=blogs)