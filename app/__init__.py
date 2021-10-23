from flask import Flask
from flask_cors import CORS
from api.routes import api
from site.routes import site
app = Flask(__name__)

app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(site)

CORS(app)

cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})
