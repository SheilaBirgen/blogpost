from flask import render_template,request,Blueprint
from pitcher.models import app
 

main = Blueprint("main",__name__)


@main.route("/")
@main.route("/home")
def home():
    posts = Pitch.query.all()
    return render_template("home.html",posts.posts,title="Home page")
    
       