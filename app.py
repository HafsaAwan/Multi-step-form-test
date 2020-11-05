import os
import config
from flask import Flask, render_template, redirect, url_for
from models.base_model import db
from authlib.integrations.flask_client import OAuth
from flask_wtf.csrf import CSRFProtect

web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'instagram_web')

app = Flask('NEXTAGRAM', root_path=web_dir)

csrf = CSRFProtect(app)

if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")


oauth = OAuth()
oauth.init_app(app)


oauth.register('facebook',
    client_id=app.config.get("FACEBOOK_APP_ID"),
    client_secret=app.config.get("FACEBOOK_APP_SECRET"),
    access_token_url='https://graph.facebook.com/v8.0/oauth/access_token',
    access_token_params=None,
    refresh_token_url=None,
    authorize_url='https://www.facebook.com/v8.0/dialog/oauth',
    api_base_url='https://www.facebookapis.com/oauth2/v1/',
    client_kwargs={}
)

@app.route("/")
def index():
  return render_template("home.html")

@app.route("/facebook_login")
def facebook_login():
  redirect_uri = url_for('authorize', _external = True)
  return oauth.facebook.authorize_redirect(redirect_uri)

@app.route("/sessions/authorize/facebook")
def authorize():
  oauth.facebook.authorize_access_token()
  result = oauth.facebook.get('https://graph.facebook.com/me').json()
  return result['name']

  
@app.before_request
def before_request():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc
