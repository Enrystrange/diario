# Import
from flask import Flask, render_template,request, redirect
# Importare la libreria del database
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Collegamento con SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creare un DB
db = SQLAlchemy(app )

# Consegna #1. Creare un DB
class Card(db.Model):
    # Creazione dei campi
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Titolo
    title = db.Column(db.String(100), nullable=False)
    # Sottotitolo
    subtitle = db.Column(db.String(300), nullable=False)
    # Testo
    text = db.Column(db.Text, nullable=False)

    # Visualizzazione dell'oggetto e del suo id
    def __repr__(self):
        return f'<Card {self.id}>'


# Esecuzione della pagina con il contenuto
@app.route('/')
def index():
    # Visualizzazione degli oggetti del DB
    # Consegna #2. Visualizzare gli oggetti del DB in index.html
    # Consegna #2. Crea un modo per memorizzare i dati nel DB


    return render_template('index.html',
                           #cards = cards

                           )

# Esecuzione della pagina con la scheda
@app.route('/card/<int:id>')
def card(id):
    # Consegna #2. Mostrare la scheda giusta in base al suo id

    cards = Card.query.order_by(Card.id).all()

    return render_template('index.html', cards=cards)
# Esecuzione della pagina e creazione della scheda
@app.route('/create')
def create():
    return render_template('create_card.html')

# Il modulo della scheda
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Consegna #2. Creare un modo per memorizzare i dati nel DB
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()




        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)