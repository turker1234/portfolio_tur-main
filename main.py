# Import
from flask import Flask, render_template,request, redirect
# Veri tabanı kitaplığını bağlama
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# SQLite'ı bağlama
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Veri tabanı oluşturma
db = SQLAlchemy(app)

class Kullanici(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mail = db.Column(db.String(30),nullable=False)
    feedback = db.Column(db.String(30),nullable=False)
# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    
    
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_db=button_db,button_html=button_html )

@app.route('/feedback', methods=['POST'])
def feedback_form():
    if request.method == 'POST':
        mail= request.form['email']
        feedback = request.form['text']
        
        # Kullanıcı verilerinin veri tabanına kaydedilmesini sağlayın
        kullanici = Kullanici(mail=mail, feedback=feedback)
        db.session.add(kullanici) # eklemek
        db.session.commit() # kaydetmek
        return redirect('/')
    

if __name__ == "__main__":
    app.run(debug=True)
