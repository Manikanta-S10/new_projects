from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)
app.secret_key = "Manikanta"

class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(250),unique=True,nullable=False)
    author:Mapped[str] = mapped_column(String(100),nullable=False)
    rating:Mapped[float] = mapped_column(Float,nullable=False)

with app.app_context():
    db.create_all()

all_books = []

@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.id))
    all_books = result.scalars().all()
    return render_template('index.html', new_books = all_books)


@app.route("/add",methods=['GET','POST'])
def add():
    if request.method == 'POST':
        new_book = Book(title=request.form['title'],author=request.form['author'],rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()   
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/changeRating',methods=["GET","POST"])
def change():
    if request.method == "POST":
        book_id = request.form["id"]
        new_rating = request.form['rating']
        try:
            new_rating = float(new_rating)  # Convert the rating to a float
        except ValueError:
            return "Invalid rating value. Please enter a valid number."
        book_to_update = db.get_or_404(Book,book_id)
        book_to_update.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    # If the request method is GET, fetch the book and pass it to the template
    book_id = request.args.get("id")  # Get the book ID from the query string
    book = db.get_or_404(Book, book_id)  # Fetch the book object
    return render_template('changerating.html',book=book)

@app.route('/deleteRow')
def delete():
    book_id = request.args.get("id")
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

