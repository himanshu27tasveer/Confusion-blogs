import os
import secrets
from flask import url_for, current_app
from PIL import Image
from flaskblog import mail
from flask_mail import Message



def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Reset your Password',
                   sender='himanshu27.stu@gmail.com',
                   recipients=[user.email])
    msg.body = f'''To reset yout password kindly click on the link :

{ url_for('users.reset_password', token=token, _external=True) }

If you did not make this request, Please ignore this mail and no changes will be made.

'''
    mail.send(msg)