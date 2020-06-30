from flask import Flask, request, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    # date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        prayer_content = request.form['content']

        new_prayer = Todo(content=prayer_content)

        try: 
            db.session.add(new_prayer)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your prayer'

    else:
        prayers = Todo.query.all()
        return render_template('index.html', prayers=prayers)

@app.route('/delete/<int:id>')
def delete(id):
    prayer_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(prayer_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that prayer'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    prayer = Todo.query.get_or_404(id)
    if request.method == 'POST':
        prayer.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your prayer'
    else:
        return render_template('update.html', prayer=prayer)

    try:
        db.session.delete(prayer_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that prayer'

@app.route('/welcome')
def welcome():
        return render_template('welcome.html')

@app.route('/contact')
def contact():
        return render_template('contact.html')

@app.route('/missionaries')
def missionaries():
        return render_template('missionaries.html')

@app.route('/faithpromise')
def faithpromise():
        return render_template('faithpromise.html')


@app.route('/gallery')
def gallery():
        return render_template('gallery.html')

if __name__ == "__main__":
    app.run(debug=True)