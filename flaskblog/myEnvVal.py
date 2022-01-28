import os


def setVar():
    os.environ['EMAIL_USER'] = 'ibanezed123@gmail.com'
    os.environ['EMAIL_PASS'] = '1'
    os.environ['SECRET_KEY'] = '4251ccddba25ca210714d97067800cdc'
    os.environ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'