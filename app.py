from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/NICOLAS/Desktop/BLOG/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Post(db.Model):
	__tablename__ = "posts"
	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String, nullable=False)
	fecha = db.Column(db.DateTime, default=datetime.now)
	texto = db.Column(db.String, nullable=False)

@app.route("/segundo.html")
def segundo():
	posts = Post.query.order_by(Post.fecha.desc()).all() 
	return render_template("segundo.html", posts=posts)

@app.route ('/')
def inicio ():
    
    
    return render_template('index.html')

@app.route("/agregar")
def agregar():
	return render_template("agregar.html")

@app.route ('/informacion')
def informacion():
    

    return render_template('informacion.html')

@app.route ('/contactos.html')
def contactos():
    
    return render_template('contactos.html') 

@app.route ('/preguntasfrecuentes.html')
def preguntasfrecuentes():
    
    return render_template('preguntasfrecuentes.html') 

@app.route ('/Post/post.html')
def post():
  
    
    return render_template('Post/post.html')    

@app.route ('/Post/post1.html')
def post1():
  
    
    return render_template('Post/post1.html') 

@app.route ('/Post/post2.html')
def post2():
  
    
    return render_template('Post/post2.html')           
        

@app.route("/crear", methods=["POST"])
def crear_post():
	titulo = request.form.get("titulo")
	texto = request.form.get("texto")
	post = Post(titulo=titulo, texto=texto)
	db.session.add(post)
	db.session.commit()
	return redirect("/segundo.html")

@app.route("/borrar", methods=["POST"])
def borrar():
	post_id = request.form.get("post_id")
	post = db.session.query(Post).filter(Post.id==post_id).first()
	db.session.delete(post)
	db.session.commit()
	return redirect("/segundo.html")


if __name__ == "__main__":
	app.run(debug=True)

