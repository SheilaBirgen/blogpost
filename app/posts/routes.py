from flask import render_template,request,url_for,redirect,request,abort, Blueprint)
from fask_login import current_user,login_required
from .forms import PostForm,CommentForm
from flask_login import login_required,current_user
from .. import db,photos

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Pitch(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template("post.html", title = "New post", form=form)