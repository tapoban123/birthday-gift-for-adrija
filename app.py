from flask import Flask, render_template
from database import wish_import_from_db, img_import_from_db, import_goods_about_you_from_db

app = Flask(__name__)


@app.route('/')
def Hello_Adrija():
    wish_data = wish_import_from_db()
    img_binary_data = img_import_from_db()
    bests_of_her = import_goods_about_you_from_db()
    return render_template('home.html', wishing=wish_data, img_data=img_binary_data, best_things=bests_of_her)


@app.route('/smile')
def Smile():
    return render_template('smile.html')

@app.route('/bday_cake')
def BDay_Cake():
    return render_template('bday_cake.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, load_dotenv=True)