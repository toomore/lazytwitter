# -*- coding: utf-8 -*-
import setting
from flask import Flask
from flask import request
from requests_oauthlib import OAuth1Session


app = Flask(__name__)
oauth_session = OAuth1Session(
        setting.client_key,
        client_secret=setting.client_secret,
        callback_uri=setting.callback_uri)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/twitter")
def twitter_url():
    oauth_session.fetch_request_token(setting.request_token_url)
    return u'<a href="%(url)s">%(url)s</a>' % dict(url=oauth_session.authorization_url(setting.authorization_url))

@app.route("/twitter_back")
def twitter_back():
    oauth_session.parse_authorization_response(request.url)
    return u'%s' % oauth_session.fetch_access_token(setting.access_token_url)

if __name__ == "__main__":
    app.run()
