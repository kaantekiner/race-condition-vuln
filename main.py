import flask
import threading
from flask import render_template
app = flask.Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html', kupon_hakki=kupon_hakki)

@app.route('/kupon_kullan')
def kupon_kullan():
    global kupon_hakki
    global kullanilan_kupon
    if kupon_hakki == 0:
        return "kullanılan kupon: " + str(kullanilan_kupon) + "<br>" + "kalan kupon hakki: " + str(kupon_hakki) + "<br><br>" + "malesef tüm kuponlarınız bitmiş..."
    else:
        threading.Thread(target=kupon_kullan).start()
        # kupon_kullan()
        return "kullanılan kupon: " + str(kullanilan_kupon) + "<br>" + "kalan kupon hakki: " + str(kupon_hakki) + "<br><br>" + "kuponunuz vardı, kullanıldı!!!"

def kupon_kullan():
    global kupon_hakki
    global kullanilan_kupon
    kullanilan_kupon += 1
    kupon_hakki -= 1
    pass

# globals
kupon_hakki = 300
kullanilan_kupon = 0
if __name__ == '__main__':
    app.run(debug=True, port=8000, host="127.0.0.1")







