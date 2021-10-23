from flask import Blueprint, request,render_template,Flask

site = Blueprint("site", __name__, template_folder="templates",
                 static_folder="static")

@site.route("/")
def index():
    return render_template("index.html")
