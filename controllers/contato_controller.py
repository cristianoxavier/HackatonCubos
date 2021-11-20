from flask_mail import Message
from configurations.enviroment import EMAIL


def envia_email(*args):
    msg = Message('Hello', sender=EMAIL, recipients=[EMAIL])
    msg.body = "Hello Flask message sent from Flask-Mail"
    return msg
