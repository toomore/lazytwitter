# -*- coding: utf-8 -*-
import setting
import twitter
from flask import Flask
from flask import redirect
from flask import request
from flask import session
from flask import url_for
from requests_oauthlib import OAuth1Session
from usertoken import Usertoken


app = Flask(__name__)
app.secret_key = setting.SESSION_KEY

#@app.route("/")
#def home():
#    return "Hello World!"

@app.route("/")
def login():
    login = u'<a href="%(url)s">Login</a>' % dict(url=url_for('get_login_url', auth_method='login'))
    create = u'<a href="%(url)s">Create</a>' % dict(url=url_for('get_login_url'))
    return u'%s / %s' % (login, create)

@app.route("/get_login_url/", defaults={'auth_method': 'create'})
@app.route("/get_login_url/<auth_method>")
def get_login_url(auth_method):
    oauth_session = OAuth1Session(
            setting.client_key,
            client_secret=setting.client_secret,
            callback_uri=setting.callback_uri)
    oauth_session.fetch_request_token(setting.request_token_url)
    if auth_method == 'create':
        return redirect(oauth_session.authorization_url(setting.authorize_url))
    else:
        return redirect(oauth_session.authorization_url(setting.authenticate_url))

@app.route("/twitter_back")
def twitter_back():
    if not request.args.get('denied'):
        oauth_session = OAuth1Session(
                setting.client_key,
                client_secret=setting.client_secret,
                callback_uri=setting.callback_uri)
        oauth_session.parse_authorization_response(request.url)
        #return u'%s' % oauth_session.fetch_access_token(setting.access_token_url)
        # key: oauth_token_secret, oauth_token, user_id, screen_name
        token_data = oauth_session.fetch_access_token(setting.access_token_url)
        session.update(token_data)

        with Usertoken() as usertoken:
            usertoken.add_token(**token_data)

        return redirect(url_for('tweet'))
    else:
        return u'取消授權'

@app.route("/tweet", methods=['GET', 'POST'])
def tweet():
    if request.method == 'GET':
        return u'<form method="POST">Hi %s<br><textarea name="content"></textarea><br><input type="submit"></form>' % session['screen_name']
    elif request.method == 'POST':
        if request.form.get('content'):
            twitter_api = twitter.Api(consumer_key=setting.client_key,
                consumer_secret=setting.client_secret,
                access_token_key=session['oauth_token'],
                access_token_secret=session['oauth_token_secret'])
            return u'%s' % twitter_api.PostUpdate(request.form['content'])
        return u'No content.'

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

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
