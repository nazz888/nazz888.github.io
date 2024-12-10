from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ana sayfa
@app.route('/')
def home():
    return render_template('index.html')

# Hayran mektupları formu
@app.route('/hayran_mektuplari', methods=['GET', 'POST'])
def hayran_mektuplari():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Mektubu bir dosyaya kaydet
        with open('mektuplar.txt', 'a', encoding='utf-8') as file:
            file.write(f"Ad: {name}\nE-posta: {email}\nMesaj: {message}\n{'-'*40}\n")
        
        return redirect(url_for('success'))
    return render_template('hayran_mektuplari.html')

# Başarı sayfası
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
