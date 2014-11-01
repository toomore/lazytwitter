# -*- coding: utf-8 -*-
#import twitter
import requests
import time
from requests_oauthlib import OAuth1Session

client_key = '4WhKjFWfep6s44uhpZsnRlZ7g'
client_secret = 'aetTFRoRGJzRDMckhn3tMTLeUSVGaYqgG4I2fCCyarpSbT6Zqk'
callback_uri = 'http://lazytwitter.toomore.net/'
request_token_url = 'https://api.twitter.com/oauth/request_token'
authorization_url = 'https://api.twitter.com/oauth/authorize'
access_token_url = 'https://api.twitter.com/oauth/access_token'

#api = twitter.Api('4WhKjFWfep6s44uhpZsnRlZ7g', 'aetTFRoRGJzRDMckhn3tMTLeUSVGaYqgG4I2fCCyarpSbT6Zqk', '12717952-9WxZbTrjk3UZy5juErRFo9X3FDYrMKcp54VH82iZK', 'c2nL0Ofg8uFKd1byuEt451BrqlNfsZGyGpJ7fguMkRPgH')
#print api.VerifyCredentials()

## ref
## http://requests-oauthlib.readthedocs.org/en/latest/api.html
oauth_session = OAuth1Session(client_key,client_secret=client_secret, callback_uri=callback_uri)
print oauth_session.fetch_request_token(request_token_url)

## Get oauth url
print oauth_session.authorization_url(authorization_url)

back_url = 'http://lazytwitter.toomore.net/?oauth_token=ReMTnJjRieKxKeDxsoor8lx81Cuu7lis&oauth_verifier=UKohoB8o0hf3wviUnxhUGcht8YAvi5MY'
print oauth_session.parse_authorization_response(back_url)

print oauth_session.fetch_access_token(access_token_url)
