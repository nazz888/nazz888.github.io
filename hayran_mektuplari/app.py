from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hayran_mektuplari.html')

@app.route('/hayran_mektuplari', methods=['POST'])
def hayran_mektuplari():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        return "Tüm alanlar doldurulmalıdır!", 400

    print(f"Ad: {name}, E-posta: {email}, Mesaj: {message}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/tesekkur')
def tesekkur():
    return "Mektubunuz için teşekkür ederiz!"
if __name__ == '__main__':
    app.run(debug=True)
