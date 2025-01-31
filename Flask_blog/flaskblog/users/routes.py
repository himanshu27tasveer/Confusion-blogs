
from flask import render_template, flash, redirect, url_for, Blueprint, request
from flaskblog import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog.models import User, Post
from flaskblog.users.utils import save_picture, send_reset_email
from flaskblog.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm





users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('Current User have to logout first.', 'danger')
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode()
        user = User(username = form.username.data, email = form.email.data, password = hashed_pass )
        db.session.add(user)
        db.session.commit()
        flash('Account has been created, You can now login', 'success')
        return redirect( url_for('users.login') )
    return render_template("register.html", title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('User is already logged in.', 'success')
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next') 
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash("Login Failed", 'danger')
    return render_template("login.html", title='Login', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template("account.html", image_file=image_file, form=form)


@users.route("/user/<string:username>")
def user_post(username):
    page = request.args.get('page', 1, type=int)
    user  = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("user_posts.html", posts=posts, user=user)

@users.route("/request_reset", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        flash('Please Logout first to reset your password.', 'danger')
        return redirect(url_for('main.home'))
    form = RequestResetForm()   
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('Email has been sent plese go to your mail for further instruction', 'success')
        return redirect( url_for('users.login') )
    return render_template('request_reset.html', form=form, title='Request Password Reset')


@users.route("/request_reset/<token>", methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        flash('Please Logout first to reset your password.', 'warning')
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('This is an invalid or expired link.', 'danger')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode()
        user.password = hashed_pass
        db.session.commit()
        flash('Your passwor has been changed, You can now login', 'success')
        return redirect( url_for('users.login') )
    return render_template('reset_password.html', form=form, title='Reset Password')