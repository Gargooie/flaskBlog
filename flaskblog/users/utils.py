import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail



def save_picture(form_pic):
    random_hex_is=secrets.token_hex()
    _,file_extension= os.path.splitext(form_pic.filename)
    pic_filename= random_hex_is + file_extension
    pic_path=os.path.join(current_app.root_path, 'static/profile_pics', pic_filename)
    output_sizes= (125,125)
    image= Image.open(form_pic)
    image.thumbnail(output_sizes)
    image.save(pic_path)

    return pic_filename


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f''' To reset your password
    {url_for('users.reset_token', token=token, _external=True)}

If you didn't make the requst just ignore the message
'''
    mail.send(msg)