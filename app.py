# -*- coding: utf-8 -*-
import setting
import twitter
from flask import Flask
from flask import request
from flask import session
from requests_oauthlib import OAuth1Session


app = Flask(__name__)
app.secret_key = setting.SESSION_KEY

@app.route("/")
def home():
    return "Hello World!"

@app.route("/login")
def twitter_url():
    oauth_session = OAuth1Session(
            setting.client_key,
            client_secret=setting.client_secret,
            callback_uri=setting.callback_uri)
    oauth_session.fetch_request_token(setting.request_token_url)
    login = u'<a href="%(url)s">Login</a>' % dict(url=oauth_session.authorization_url(setting.authenticate_url))
    create = u'<a href="%(url)s">Create</a>' % dict(url=oauth_session.authorization_url(setting.authorize_url))
    return u'%s / %s' % (login, create)

@app.route("/twitter_back")
def twitter_back():
    oauth_session = OAuth1Session(
            setting.client_key,
            client_secret=setting.client_secret,
            callback_uri=setting.callback_uri)
    oauth_session.parse_authorization_response(request.url)
    #return u'%s' % oauth_session.fetch_access_token(setting.access_token_url)
    # key: oauth_token_secret, oauth_token, user_id, screen_name
    token_data = oauth_session.fetch_access_token(setting.access_token_url)
    session.update(token_data)
    return u'%s' % session

@app.route("/twitter_test_post")
def twitter_test_post():
    twitter_api = twitter.Api(consumer_key=setting.client_key,
        consumer_secret=setting.client_secret,
        access_token_key=setting.oauth_token,
        access_token_secret=setting.oauth_token_secret)

    return u'%s' % twitter_api.PostUpdate(u'只有 coordinates 資訊呢？',
            place_id='204a435ce97d5de4',
            latitude='25.0358461',
            longitude='121.45030159999999',
            display_coordinates=True)

if __name__ == "__main__":
    app.run(debug=True)
