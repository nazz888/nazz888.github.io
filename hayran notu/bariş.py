from flask import Flask, request, render_template

app = Flask(__name__)

# Notları saklamak için bir liste (geçici)
notlar = []

@app.route('/')
def anasayfa():
    return render_template('index.html', notlar=notlar)

@app.route('/gonder', methods=['POST'])
def gonder():
    isim = request.form.get('isim')
    mesaj = request.form.get('mesaj')
    if isim and mesaj:
        notlar.append({'isim': isim, 'mesaj': mesaj})
    return render_template('index.html', notlar=notlar)

if __name__ == '__main__':
    app.run(debug=True)
