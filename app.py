from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')  # SQLite database file: todo_app.db
    # postgres://tododb_lwlb_user:xo5LblHGjwWa15QWTYkFvFkMWGgU6D2W@dpg-cj55t1k5kgrc738ph6kg-a.oregon-postgres.render.com/tododb_lwlb
    return app
app = create_app()
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed =db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    
    def __repr__(self):
        return '<task %r>' % self.id
    # Your model definition remains the same

# Your database creation code can be moved to a function to make it more organized
def create_database():
    with app.app_context():
        db.create_all()

if not os.path.exists('todo_app.db'):
    create_database()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content = task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding ur task'
            
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)    
    try:
         db.session.delete(task_to_delete)
         db.session.commit()
         return redirect('/')
    except:
        return 'there was a problem deleting that task'
    
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'there was an issue updating that task'
            
    else :
        return render_template('update.html', task = task)
    

if __name__ == '__main__':
    app.run(debug=True)
