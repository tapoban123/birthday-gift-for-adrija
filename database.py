from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from os import environ
import base64

load_dotenv('.env')

USERNAME = environ.get('USER')
PASSWORD = environ.get('PASSWORD')
HOSTNAME = environ.get('HOST')
DB_NAME = environ.get('DATABASE')

conn_str = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DB_NAME}?charset=utf8mb4"

engine = create_engine(conn_str, connect_args={
    'ssl': {
        'ssl_ca': "/etc/ssl/cert.pem"
    }
})


def wish_import_from_db():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM WISHING;"))
        data = result.fetchone()

    wish_words_list = [word for word in data[0].split()]
    return wish_words_list


def binaryToImage(filepath, binary_data):
    with open(filepath, mode='wb') as file:
        file.write(binary_data)


def img_import_from_db():
    with engine.connect() as connection:
        result = connection.execute(text('SELECT * FROM IMAGES;'))
        data = result.all()
    
    binary_data_of_images = []

    for img_data in data:
        binary_data_of_images.append(img_data[1].decode('utf-8'))

    return binary_data_of_images


def import_goods_about_you_from_db():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM GOOD17;"))
        data = result.all()

    best_of_you = [good[1] for good in data]
    return best_of_you

# print(img_import_from_db())
# print(wish_import_from_db())
import_goods_about_you_from_db()
    